# -*- coding: UTF-8 -*-

"""
The api https://docs.python.org/3.8/library/xml.dom.html#xml.dom.NodeList.item
"""
from xml.dom.minidom import parse

# import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
# DOMTree = xml.dom.minidom.parse("demo.xml")

DOMTree = parse("demo.xml")
# DOMTree.documentElement : The one and only root element of the document.
root = DOMTree.documentElement

if root.hasAttribute("shelf"):
    print("Root element : %s" % root.getAttribute("shelf"))

# 在集合中获取所有电影
movies = root.getElementsByTagName("movies")

# 打印每部电影的详细信息
for movie1 in movies:
    movieList = movie1.getElementsByTagName("movie")
    for movie in movieList:
        print("*****Movie*****")
        if movie.hasAttribute("title"):
            print("Title: %s" % movie.getAttribute("title"))

        type = movie.getElementsByTagName('type')[0]
        print("Type: %s" % type.childNodes[0].data)
        format = movie.getElementsByTagName('format')[0]
        print("Format: %s" % format.childNodes[0].data)
        rating = movie.getElementsByTagName('rating')[0]
        print("Rating: %s" % rating.childNodes[0].data)
        description = movie.getElementsByTagName('description')[0]
        print("Description: %s" % description.childNodes[0].data)
