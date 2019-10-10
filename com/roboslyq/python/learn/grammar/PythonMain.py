# python入门学习入口函数
"""
于20190.10.10创建
"""


import BasicLearn
import VariableLearn
import ClassLearn


if __name__ == '__main__':
    BasicLearn.printf("lyq")
    VariableLearn.cal(1, 2)
    hw = VariableLearn.HelloWorld()
    hw.sayhello()
    """
    类测试
    1、init方法重载不太方便
    """
    stu = ClassLearn.Student(70)
    stu1 = ClassLearn.Student(80)
    print(stu.getageband())
    print(stu1.getageband())
