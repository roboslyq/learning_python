# python入门学习入口函数
"""
于20190.10.10创建
"""


import basic_grammar_demo
import variable_demo
import class_demo


if __name__ == '__main__':
    basic_grammar_demo.printf("lyq")
    variable_demo.cal(1, 2)
    hw = variable_demo.HelloWorld()
    hw.sayhello()
    """
    类测试
    1、init方法重载不太方便
    """
    stu = class_demo.Student(70)
    stu1 = class_demo.Student(80)
    print(stu.getageband())
    print(stu1.getageband())
