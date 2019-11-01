"""
一次性读全部
"""
import os


def readfile_original():
    try:
        f = open('D:\\python_workspace\\test.txt', 'r', encoding='UTF-8')
        print(f.read())
    except FileNotFoundError:
        print("文件不存在")
        # finally:
    # if f:
    #     f.close()


def readfile_new():
    """
    默认关闭文件流形式
    :return:
    """
    with open('D:\\python_workspace\\test.txt', 'r', encoding='UTF-8') as f:
        print(f.read())


"""
按行读
"""


def readLine():
    with open('D:\\python_workspace\\test.txt', 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            print(line.strip())

# 当前py文件所在的绝对路径
curPath=os.path.abspath(os.path.dirname(__file__))
print(curPath)

# 当前项目根路径
rootPath = curPath[:curPath.find("learning_python\\")+len("learning_python\\")]
print(rootPath)
# 获取xxx文件路径

xxx_file_path = os.path.abspath(rootPath+"com\\__init__.py")

print(xxx_file_path)
# 传统语法


readfile_original()

# 新语法


readfile_new()
# 按行读


readLine()
