"""通过正则表达式进行相关处理
"""
# !/usr/bin/python
# -*- coding: UTF-8 -*-

import re

print(re.match("(a)(.*?)", "aaabbabababaaaab").group(0))
print(re.match("(a)*", "aaabbabababaaaab").group(1))
# print(re.match("(a)*", "aaabbabababaaaab").group(2))
# print(re.match("(a)*", "aaabbabababaaaab").group(3))
# print(re.match("(a)(.*?)", "aaabbabababaaaab").group(4))


pattern1 = "(<img .*?src=\")(.*?)(\")"

for i in range(0, 10):
    print(i)


def func1(m):
    print("group(0):" + m.group(0))
    print("group(1):" + m.group(1))
    print("group(2):" + m.group(2))
    print("group(3):" + m.group(3))
    # print("group(3):" + m.group(4))
    if not m.group(2).startswith("https"):
        rtn = m.group(1) + "https:" + m.group(2) + m.group(3)
        return rtn
    else:
        return m.group(1) + m.group(2) + m.group(3)


htmlString = '''<img src="https://www.runoob.com/wp-content/uploads/2014/12/pycharm-utf8.jpg">
<img src="//www.runoob.com/wp-content/uploads/2014/12/pycharm-utf8.jpg">
'''

html = re.compile(pattern1).sub(func1, htmlString)
print(html)
