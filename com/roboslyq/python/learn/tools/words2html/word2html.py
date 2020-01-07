from pydocx import PyDocX

"""
旧包：docx2html，此包要求python版本较低
新包路径如下：
https://github.com/CenterForOpenScience/pydocx
"""

docx_file = r'D:\十二刻度-个人信息及隐私政策.docx'
html_fle = r'D:\result.html'
html = PyDocX.to_html(docx_file)
with open(html_fle, encoding='UTF-8', mode='w') as f:
    f.write(html)
