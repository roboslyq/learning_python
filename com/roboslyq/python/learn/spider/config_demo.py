# 定义相关路径及配置
# 定义网页入口路径
domain_path = "https://www.liaoxuefeng.com"
base_path = "/wiki/1016959663602400"

# wkhtmltopdf工具安装位置（需要绝对路径，否则会报错）
path_wk = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
# 临时文件文件名称(未合并)
tmp_file_name = u"Python3_tutorial"
# 完成合并的最终结果文件名称
merger_file_name = u"Python3_tutorial.pdf"
# 结果文件保存路径
download_file_path = r"D:\python_workspace\git\learning_python\download" + "\\"

# 将html保存为pdf时相关配置
pdf_options = {
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

# 定义请求头，如果未定义可能导致https请求报503异常
headers = {
           "X-Member-Id": "23832170000",
           "X-Region": "1100000",
           "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
           "X-Channel": "01",
           "Content-Type": "application/jsonlearn;charset=UTF-8"
           }

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

