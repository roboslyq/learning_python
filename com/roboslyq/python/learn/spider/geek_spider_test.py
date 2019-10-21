# coding=utf-8
import logging
import os
import re
import time

import pdfkit
import requests
from PyPDF2 import PdfFileMerger
from bs4 import BeautifulSoup


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
    pdfs = []
    filanames = {"0.html": "0.pdf", "1.html": "1.pdf", "2.html": "2.pdf"}
    for srcname, targetname in filanames.items():
        save_pdf(srcname, targetname)
        pdfs.append(targetname)
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(open(pdf, 'rb'))
    output = open(u"廖雪峰Python_all.pdf", "wb")
    merger.write(output)

if __name__ == '__main__':
    main()
