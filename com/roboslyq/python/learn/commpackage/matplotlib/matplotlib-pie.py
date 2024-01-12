import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 设置字体
plt.rcParams["font.sans-serif"] = ["SimHei"]
# 该语句解决图像中的“-”负号的乱码问题
plt.rcParams["axes.unicode_minus"] = False
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


def demo_pie():
    y = np.array([35, 25, 25, 15])

    plt.pie(y)
    plt.pie(y,
            labels=['A', 'B', 'C', 'D'],  # 设置饼图标签
            colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"],  # 设置饼图颜色
            )
    plt.title("运维报告测试图")  # 设置标题
    plt.show()


if __name__ == '__main__':
    demo_pie();
