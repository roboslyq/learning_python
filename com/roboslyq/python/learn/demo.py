import logging
import os
import re
import time

pattern = "(<img .*? src=\")(.*?)(\")"
pattern1 = "(<iframe(.*?)</iframe>)"

htmlString = '''<ul id="TopNav"><li><a href="/EditPosts.aspx" id="TabPosts">随笔</a></li>
        <li><a href="/EditArticles.aspx" id="TabArticles">文章</a></li>
        <li><a href="/EditDiary.aspx" id="TabDiary">日记</a></li>
        <li><a href="/Feedback.aspx" id="TabFeedback">评论</a></li>
        <li><a href="/EditLinks.aspx" id="TabLinks">链接</a></li>
        <li id="GalleryTab"><a href="/EditGalleries.aspx" id="TabGalleries">相册</a></li>
        <li id="FilesTab"><a href="Files.aspx" id="TabFiles">文件</a></li>
        <li><a href="/Configure.aspx" id="TabConfigure">设置</a></li>
        <li><a href="/Preferences.aspx" id="TabPreferences">选项</a></li></ul>'''

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
