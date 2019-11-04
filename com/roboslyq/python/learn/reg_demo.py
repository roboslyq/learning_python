import logging
import os
import re
import time

# body中的img标签的src相对路径的改成绝对路径,注意"? src"之间有一个空格(因为有一个属性是data-src,如果不加空格会匹配到这一个属性)
pattern0 = "(<img .*?src=\")(.*?)(\")(.*?)(data-src=\")(.*?)(\")"
pattern1 = "(<img .*?data-src=\")(.*?)(\")(.*?)(src=\")(.*?)(\")"


def func1(m):
    if not m.group(2).startswith("https"):
        print("m.group(0):" + m.group(0))
        print("m.group(1):" + m.group(1))
        print("m.group(2):" + m.group(2))
        print("m.group(3):" + m.group(3))
        print("m.group(4):" + m.group(4))
        print("m.group(5):" + m.group(5))
        print("m.group(6):" + m.group(6))
        print("m.group(6):" + m.group(7))
        rtn = m.group(1) + "https:" + m.group(6) + m.group(3) + m.group(4) + m.group(5) + m.group(6)+ m.group(7)
        return rtn
    else:
        print("start  with https" + m.group(2))
        return m.group(1) + m.group(2) + m.group(3)


htmlString = '''
               <img alt="tpci_trends" data-src="a" src="b"/>
              '''

htmlString = re.compile(pattern0).sub(func1, htmlString)
html = re.compile(pattern1).sub(func1, htmlString)
print(html)
