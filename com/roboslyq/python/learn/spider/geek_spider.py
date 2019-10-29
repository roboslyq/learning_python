# coding=utf-8
import logging
import os
import re                           # 正则表达式包
import time

import pdfkit                       # pdf 工具包
import requests                     # 网络请求包
from PyPDF2 import PdfFileMerger    # pdf 合并工具包
from bs4 import BeautifulSoup       # html解析处理包

'''
python 爬虫，可以抓取网络上的文章并且保存为Pdf
'''
# 定义网页入口路径
domain_path = "https://www.liaoxuefeng.com"
base_path = "/wiki/1016959663602400"

# 定义请求头，如果未定义可能导致https请求报503异常
headers = {"X-Member-Id": "23832170000",
           "X-Region": "1100000",
           "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
           "X-Channel": "01",
           "Content-Type": "application/json;charset=UTF-8"}

# html模板，用来保存下载的html内容
html_template = """
                  <!DOCTYPE html>
                  <html lang="en">
                  <head>
                    <meta charset="UTF-8">
                  </head>
                  <body>
                  {content}
                  </body>
                  </html>
                """


"""
解析URL，返回HTML内容
:param url:解析的url
:param name: 保存的html文件名
:return: html
"""


def parse_url_to_html(url, name):
    try:
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
        html = str(body)
        # body中的img标签的src相对路径的改成绝对路径,注意"? src"之间有一个空格(因为有一个属性是data-src,如果不加空格会匹配到这一个属性)
        pattern1 = "(<img .*? src=\")(.*?)(\")"
        # iframe和img一样，如果src属性包含相对路径，则需要处理为绝对路径。否则会导致生成pdf时报NotFoundContent异常
        pattern2 = re.compile(r'(<iframe)(.*?)(</iframe>)')

        def func1(m):
            if not m.group(3).startswith("https"):
                rtn = m.group(1) + "https://www.liaoxuefeng.com" + m.group(2) + m.group(3)
                return rtn
            else:
                return m.group(1) + m.group(2) + m.group(3)

        html = re.compile(pattern1).sub(func1, html)
        # 删除iframe元素
        html = pattern2.sub(r'', html)
        # print(html)
        html = html_template.format(content=html)
        html = html.encode("utf-8")
        with open(name, 'wb') as f:
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
        # if len(urls) < 3:  # 调度时限定3个文件
        url = domain_path + tag.get('href')
        urls.append(url)
    return urls


def save_pdf(htmls, file_name):
    """
    把所有html文件保存到pdf文件
    :param htmls: html文件列表
    :param file_name: pdf文件名
    :return:
    """
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        # 'outline-depth': 10000000,
    }
    path_wk = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # 安装位置
    config = pdfkit.configuration(wkhtmltopdf=path_wk)
    # 此处需要绝对路径
    htmls = r"D:\helloworld\workspace_python\learning_python\com\roboslyq\python\learn\spider" + "\\" + htmls
    pdfkit.from_file(htmls, file_name, options=options, configuration=config)


def main():
    start = time.time()
    file_name = u"liaoxuefeng_Python3_tutorial"
    urls = get_url_list()
    for index, url in enumerate(urls):
        parse_url_to_html(url, str(index) + ".html")
    htmls = []
    pdfs = []
    for i in range(0, len(urls) - 1):
        htmls.append(str(i) + '.html')
        pdfs.append(file_name + str(i) + '.pdf')
        save_pdf(str(i) + '.html', file_name + str(i) + '.pdf')
        print(u"转换完成第" + str(i) + '个html')
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(open(pdf, 'rb'))
        print(u"合并完成第" + str(i) + '个pdf' + pdf)
    output = open(u"廖雪峰Python_all.pdf", "wb")
    merger.write(output)
    print
    u"输出PDF成功！"
    for html in htmls:
        os.remove(html)
        print
        u"删除临时文件" + html
    for pdf in pdfs:
        os.remove(pdf)
        print
        u"删除临时文件" + pdf
    total_time = time.time() - start
    print(u"总共耗时：%f 秒" % total_time)


if __name__ == '__main__':
    main()
