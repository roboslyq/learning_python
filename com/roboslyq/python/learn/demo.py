import logging
import os
import re
import time

# body中的img标签的src相对路径的改成绝对路径,注意"? src"之间有一个空格(因为有一个属性是data-src,如果不加空格会匹配到这一个属性)
pattern1 = "(<img .*?src=\")(.*?)(\")"
# iframe和img一样，如果src属性包含相对路径，则需要处理为绝对路径。否则会导致生成pdf时报NotFoundContent异常
pattern2 = re.compile(r'(<iframe)(.*?)(</iframe>)')


def func1(m):
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




pattern = "(<img .*? src=\")(.*?)(\")"
pattern1 = "(<iframe(.*?)</iframe>)"


# 方法 1
pre = re.compile('>(.*?)<')
s1 = ''.join(pre.findall(htmlString))
print(s1)  # '随笔文章日记评论链接相册文件设置选项'

iframe = "<p><iframe border=\"0\" frameborder=\"no\" framespacing=\"0\" scrolling=\"no\" src=\"//player.bilibili.com/player.html?aid=51230273\" style=\"width:100%;height:480px\"></iframe></p>"
reg_iframe = re.compile(r'(<iframe)(.*?)(</iframe>)')
print(reg_iframe.sub(r'',iframe))
#
# def func1(m):
#     return m.group(1) + m.group(3)
#
#
# def func(m):
#     if not m.group(3).startswith("https"):
#         rtn = m.group(1) + "https://www.liaoxuefeng.com" + m.group(2) + m.group(3)
#         return rtn
#     else:
#         return m.group(1) + m.group(2) + m.group(3)
#
#
# html = re.compile(pattern).sub(func,
#                                "<img alt=\"challenge-accepted\" data-src=\"attachments/922915342925824/0\" src=\"/static/img/loading.svg\"/>"
#                                "<img alt=\"challenge-accepted\" data-src=\"attachments/922915342925824/0\" src=\"/static/img/loading.svg\"/>")
# html = re.compile(pattern).sub(func, html)
# print(html)
#
# print(re.compile(pattern1).sub(func1,  "bb<iframe alt=\"challenge-accepted\" data-src=\"attachments/922915342925824/0\" src=\"/static/img/loading.svg\"/></iframe>dd"))
