# coding=utf-8
import logging
import os
import re
import time

import pdfkit
import requests
from PyPDF2 import PdfFileMerger
from bs4 import BeautifulSoup

headers = {"X-Member-Id": "23832170000",
           "X-Region": "1100000",
           "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
           "X-Channel": "01",
           "Content-Type": "application/json;charset=UTF-8"}

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


def parse_url_to_html(url, name):
    """
    解析URL，返回HTML内容
    :param url:解析的url
    :param name: 保存的html文件名
    :return: html
    """
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup.prettify())
        # 正文
        # body = soup.find_all(class_="x-wiki-content")[0]
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
        # body中的img标签的src相对路径的改成绝对路径,注意"? src"之间有一个空格
        pattern1 = "(<img .*? src=\")(.*?)(\")"

        def func1(m):
            if not m.group(3).startswith("https"):
                rtn = m.group(1) + "https://www.liaoxuefeng.com" + m.group(2) + m.group(3)
                return rtn
            else:
                return m.group(1) + m.group(2) + m.group(3)

        html = re.compile(pattern1).sub(func1, html)

        print(html)
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

    response = requests.get("https://www.liaoxuefeng.com/wiki/1016959663602400", headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    # print(soup.prettify())
    # menu_tag = soup.find_all(class_="x-wiki-index-item")[1]
    menu_tag = soup.find_all(id="x-wiki-index")[0]
    urls = []
    for tag in menu_tag.find_all("a"):
        if len(urls) < 3:  # 调度时限定3个文件
            url = "https://www.liaoxuefeng.com" + tag.get('href')
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
    for i in range(0, 124):
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
