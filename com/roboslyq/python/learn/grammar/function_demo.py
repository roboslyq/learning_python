"""
  函数学习
"""


def calc(val1, val2):
    """
    返回一个元素的函数
    :type val1: object
    """
    return val2 + val1


def calc1(val1, val2):
    """
    返回多个元素的函数
    :type val1: object
    """
    return val1, val2, val2 + val1


# 返回一个元素测试
val1 = 12
val2 = 24
print(calc(val1, val2))

# 返回多个元素测试
res1, res2, res3 = calc1(val1, val2)
print(res1)
print(res2)
print(res3)


# 入参为一个任意个数，python将其作为一个元组处理，使用*标识

def calc(int1, *ints):
    return int1 + sum(ints)


res4 = calc(1, 2, 3, 4, 5)
res5 = calc(1, 2, 3, 4, 5, 6, 7, 8)
print(res4)
print(res5)


# 入参为任意个数的关键字，即有变量名称的，python将其作为map处理，使用**标识

def calc2(int1, int2, **keyvalue):
    print(int1 + int2)
    for key, val in keyvalue.items():
        print(key + ":" + val)


"""
调用方式如下：使用k=v的方式，传入多个参数
"""
calc2(1, 2, k1="v1", k2="v2")

"""
lambda函数
"""
addLambda = lambda x, y: x + y
print(addLambda(1, 2))
