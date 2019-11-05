# coding=utf-8
import logging
import os
import re  # 正则表达式包
import time

import pdfkit  # pdf 工具包
import requests  # 网络请求包
from PyPDF2 import PdfFileMerger  # pdf 合并工具包
from bs4 import BeautifulSoup  # html解析处理包

from com.roboslyq.python.learn.spider.config_demo import *

'''
python 爬虫Demo，抓取网络上的文章并且保存为Pdf。
'''


def reg_html(html):
    """
    处理html文件中的相对路径（如果不处理，生成pdf报错 ,常见的相对路径主要是图片）
    :param html:
    :return:
    """
    # body中的img标签的src相对路径的改成绝对路径,注意"? src"之间有一个空格(因为有一个属性是data-src,如果不加空格会匹配到这一个属性)
    pattern0 = "(<img .*?src=\")(.*?)(\")(.*?)(data-src=\")(.*?)(\")"
    pattern1 = "(<img .*?data-src=\")(.*?)(\")(.*?)(src=\")(.*?)(\")"
    # iframe和img一样，如果src属性包含相对路径，则需要处理为绝对路径。否则会导致生成pdf时报NotFoundContent异常
    pattern2 = re.compile(r'(<iframe)(.*?)(</iframe>)')

    def func0(m):
        if not m.group(2).startswith("https"):
            rtn = m.group(1) + domain_path + m.group(6) + m.group(3) + m.group(4) + m.group(5) + m.group(
                6) + m.group(7)
            return rtn
        else:
            return m.group(1) + m.group(2) + m.group(3) + m.group(4) + m.group(5) + m.group(6) + m.group(7)

    def func1(m):
        if not m.group(2).startswith("https"):
            rtn = m.group(1) + m.group(2) + m.group(3) + m.group(4) + m.group(5) + domain_path + m.group(
                2) + m.group(7)
            return rtn
        else:
            return m.group(1) + m.group(2) + m.group(3) + m.group(4) + m.group(5) + m.group(6) + m.group(7)

    html = re.compile(pattern0).sub(func0, html)
    html = re.compile(pattern1).sub(func1, html)
    # 删除iframe元素
    html = pattern2.sub(r'', html)
    return html


def parse_url_to_html(url, name):
    """
    解析URL，返回HTML内容
    :param url:解析的url
    :param name: 保存的html文件名
    :return: html
    """
    try:
        print("url--" + url)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        # print(soup.prettify())
        # 正文
        # body = soup.find_all(class_="x-wiki-content")[0]
        """
        以下是根据需要下载的内容所在标签查询所有内容.具体标签内容需要根据实际情况来定。
        不同的页面标签可能不一样
        """
        body = soup.find_all(id="x-content")[0]
        # 标题
        title = soup.find('h4').get_text()
        # 标题加入到正文的最前面，居中显示
        center_tag = soup.new_tag("center")
        title_tag = soup.new_tag('h1')
        title_tag.string = title
        center_tag.insert(1, title_tag)
        body.insert(1, center_tag)
        html = reg_html(str(body))

        # print(html)
        html = html_template.format(content=html)
        html = html.encode("utf-8")
        with open(download_file_path + name, 'wb') as f:
            f.write(html)
        return name
    except Exception as e:
        logging.error("解析错误", exc_info=True)


def get_url_list():
    """
    获取所有URL目录列表
    :return:
    """
    response = requests.get(domain_path + base_path, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    # print(soup.prettify())
    # menu_tag = soup.find_all(class_="x-wiki-index-item")[1]
    menu_tag = soup.find_all(id="x-wiki-index")[0]
    urls = []
    for tag in menu_tag.find_all("a"):
        if len(urls) < 3:  # 调度时限定3个文件
            url = domain_path + tag.get('href')
            urls.append(url)
        # url = domain_path + tag.get('href')
        # urls.append(url)
    return urls


def save_pdf(htmls, file_name):
    """
    把所有html文件保存到pdf文件
    :param htmls: html文件列表
    :param file_name: pdf文件名
    :return:
    """
    config = pdfkit.configuration(wkhtmltopdf=path_wk)
    # 此处需要绝对路径
    htmls = download_file_path + htmls
    pdfkit.from_file(htmls, download_file_path + file_name, options=pdf_options, configuration=config)


def main():
    start = time.time()
    urls = get_url_list()
    for index, url in enumerate(urls):
        parse_url_to_html(url, str(index) + ".html")

    html_list = []
    pdf_list = []
    # range包左不包右
    for i in range(0, len(urls)):
        html_list.append(str(i) + '.html')
        pdf_list.append(tmp_file_name + str(i) + '.pdf')

        save_pdf(str(i) + '.html', tmp_file_name + str(i) + '.pdf')
        print(u"转换完成第" + str(i) + '个html')

    merger = PdfFileMerger()
    pdf_open_list = []
    for pdf in pdf_list:
        # with open(download_file_path + pdf, 'rb') as f:
        #     merger.append(f)
        #     print(u"合并完成第" + str(i) + '个pdf' + pdf)
        f = open(download_file_path + pdf, 'rb')
        # merger.append(file_rd, bookmark=short_filename, import_bookmarks=import_bookmarks)
        pdf_open_list.append(f)
        merger.append(f)
        # 此处不能关闭，会导致结果文件为空
        # f.close()
        print(u"合并完成第" + str(i) + '个pdf' + pdf)

    output = open(download_file_path + merger_file_name, "wb")
    merger.write(output)
    merger.close()
    # 关闭流
    for pdf_file in pdf_open_list:
        pdf_file.close()

    print(u"输出PDF成功！")
    for html in html_list:
        os.remove(download_file_path + html)
        print(u"删除临时文件" + html)

    for pdf in pdf_list:
        os.remove(download_file_path + pdf)
        print(u"删除临时文件" + pdf)
    total_time = time.time() - start
    print(u"总共耗时：%f 秒" % total_time)


if __name__ == '__main__':
    main()
