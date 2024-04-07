import math
from math import pi

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rc("font", family='YouYuan')


def demo_plot():
    """
    画线
    :return:
    """
    xargs = [1, 2, 3, 4, 5]
    data = [1, 4, 9, 16, 25]
    plt.plot(xargs, data)
    plt.title("平方")
    plt.show()


def demo_bar():
    a = ["一月份", "二月份", "三月份", "四月份", "五月份", "六月份"]
    b = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96]
    plt.figure(figsize=(20, 8), dpi=80)
    plt.bar(range(len(a)), b)
    # 绘制x轴
    plt.xticks(range(len(a)), a)
    plt.xlabel("月份")
    plt.ylabel("数量")
    plt.title("每月数量")
    plt.show()


def demo_sinx():
    data = np.arange(0, 6, 0.1)  # 以0.1为单位，生成0到6的数据
    x = math.sin(data)
    y = math.cos(data)
    plt.plot(data, x)
    plt.plot(data, y)
    plt.show()


if __name__ == '__main__':
    demo_plot()
    demo_bar()
    demo_sinx()
