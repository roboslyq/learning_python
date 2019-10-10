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
