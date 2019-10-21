import logging
import os
import re
import time

pattern = "(<img .*? src=\")(.*?)(\")"


def func(m):
    if not m.group(3).startswith("https"):
        rtn = m.group(1) + "https://www.liaoxuefeng.com" + m.group(2) + m.group(3)
        return rtn
    else:
        return m.group(1) + m.group(2) + m.group(3)


html = re.compile(pattern).sub(func, "<img alt=\"challenge-accepted\" data-src=\"attachments/922915342925824/0\" src=\"/static/img/loading.svg\"/>"
                                     "<img alt=\"challenge-accepted\" data-src=\"attachments/922915342925824/0\" src=\"/static/img/loading.svg\"/>")
html = re.compile(pattern).sub(func,html)
print(html)
