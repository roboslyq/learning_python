"""
一次性读全部
"""
def readfile_original():
    try:
        f = open('D://test.txt', 'r')
        print(f.read())
    finally:
        if f:
            f.close()


def readfile_new():
    with open('D://test.txt', 'r') as f:
        print(f.read())

"""
按行读
"""


def readLine():
    with open('D://test.txt', 'r') as f:
        for line in f.readlines():
            print(line.strip())

# 传统语法
readfile_original()
#新语法
readfile_new()
#按行读
readLine()