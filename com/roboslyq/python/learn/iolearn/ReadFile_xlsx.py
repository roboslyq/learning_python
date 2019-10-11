"""
常见的Excel读取工具包如下：
    1、用xlrd和xlwt进行excel读写；
    2、用openpyxl进行excel读写；
    3、用pandas进行excel读写；
"""
import os
import xlrd


def readfile_xlsx():
    try:
        # xlrd.open_workbook(os.path.join(filepath, excelname))
        # 读取整个excel
        f = xlrd.open_workbook("D:\\python_workspace\\test2.xls")
        # 获取第0个sheet
        sheet0 = f.sheets()[0]
        rowsnumber = sheet0.nrows  # 获取行数
        colsnumber = sheet0.ncols  # 获取列数
        for i in range(rowsnumber):
            for j in range(colsnumber):
                print(str(sheet0.row_values(i)[j])[1:3])
        return 0
    except Exception as e:
        raise e


# 传统语法
try:
    res = readfile_xlsx()
    if res == 0:
        print("成功")
    else:
        print("失败")
except Exception as e:
    print(e)
