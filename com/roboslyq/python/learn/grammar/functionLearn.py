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
