import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)

"""
以下是一些常用的 pyplot 函数：
    plot()：用于绘制线图和散点图
    scatter()：用于绘制散点图
    bar()：用于绘制垂直条形图和水平条形图
    hist()：用于绘制直方图
    pie()：用于绘制饼图
    imshow()：用于绘制图像
    subplots()：用于创建子图
"""


def demo_plot():
    """
        画单条线
        plot([x], y, [fmt], *, data=None, **kwargs)
        # 画多条线
        plot([x], y, [fmt], [x2], y2, [fmt2], ..., **kwargs)

        参数说明：
        x, y：点或线的节点，x 为 x 轴数据，y 为 y 轴数据，数据可以列表或数组。
        fmt：可选，定义基本格式（如颜色、标记和线条样式）。
        **kwargs：可选，用在二维平面图上，设置指定属性，如标签，线的宽度等。
    """
    # xpoints = np.array([0, 6])
    # ypoints = np.array([0, 100])
    # 创建 y 中数据与 x 中对应值的二维线图，使用默认样式
    # plt.plot(xpoints, ypoints)

    # 创建 y 中数据与 x 中对应值的二维线图，使用蓝色实心圈绘制
    # plt.plot(xpoints, ypoints, 'o')

    # x 的值为 0..N-1
    # plt.plot(ypoints)

    # 使用红色 + 号
    # plt.plot(ypoints, 'r+')

    #  x 的值默认设置为 [0, 1, 2, 3, 4, 5]。
    # ypoints = np.array([3, 8, 1, 10, 5, 7])
    # plt.plot(ypoints)

    # 绘制一个正弦和余弦图，在 plt.plot() 参数中包含两对 x,y 值，第一对是 x,y，这对应于正弦函数，第二对是 x,z，这对应于余弦函数。
    # 4 * np.pi = 360度，刚好一周
    x = np.arange(0, 8 * np.pi, 0.1)  # start,stop,step
    y = np.sin(x)
    z = np.cos(x)
    plt.plot(x, y, x, z)
    plt.show()

    plt.show()


if __name__ == '__main__':
    demo_plot();
