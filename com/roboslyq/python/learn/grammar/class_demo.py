class Student(object):
    """
      类测试
      1、init方法重载不太方便
    """

    def __init__(self):
        self.name = "lyq"
        self.age = 20

    def __init__(self, age):
        self.name = "lyq"
        self.age = age

    def getageband(self):
        if self.age <= 20:
            return "A"
        if 60 >= self.age > 20:
            return "B"
        else:
            return "C"


"""
多重继承
"""


class clazz1():

    def __init__(self):
        self.val = "1"

    def printVal1(self):
        print(self.val)


class clazz2():

    def __init__(self):
        self.val = "2"

    def printVal2(self):
        print(self.val)


class clazz3(clazz1, clazz2):
    pass


"""
可以看出多重继承的效果，clazz3已经拥有clazz1和clazz2的方法和相关属性
"""
test_class3 = clazz3();
test_class3.printVal1()
test_class3.printVal2()
