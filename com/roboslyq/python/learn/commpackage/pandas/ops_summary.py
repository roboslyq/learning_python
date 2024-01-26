import pandas as pd
import xlrd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'simhei'


def read_data_from_file(file_path):
    # 使用read_excel函数读取Excel文件并将其存储为DataFrame对象
    df = pd.read_excel(file_path)

    grouped_types = df['类别'].groupby(df['类别']).count()
    # 绘制柱状图
    plt.bar(grouped_types.index, grouped_types.values)
    plt.xlabel('类型')
    plt.ylabel('个数')
    plt.title('运维工单分类统计(类型维度)')
    plt.show()

    dept_types = df['所属部门'].groupby(df['所属部门']).count()
    # 绘制柱状图
    plt.bar(dept_types.index, dept_types.values)
    plt.xlabel('部门')
    plt.ylabel('个数')
    plt.title('运维工单分类统计(部门维度)')
    # 设置柱状图之间的间距为0.8（默认值为0.8）
    plt.subplots_adjust(wspace=12)
    plt.show()


if __name__ == '__main__':
    read_data_from_file(r"C:\Users\Administrator\Desktop\周报\广州资产AMC核心业务系统运维跟踪表-（From 20240101）.xls")
