"""
变量定义学习

"""


def test():
    val = 100
    for i in range(val):
        print(i)
        cal(i, 1)


def cal(va11, val2):
    print(va11 + val2)

class HelloWorld(object):
    def __init__(self):
        self.name = "hello,luoyq"

    def sayhello(self):
        print(self.name)
