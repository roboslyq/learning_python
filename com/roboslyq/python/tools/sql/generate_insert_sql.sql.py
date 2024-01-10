import pandas as pd
import sqlite3
import openpyxl


def generate_insert_sql(excel_path: str, table_name: str) -> str:
    """将 Excel 文件转化为 SQL 的 INSERT INTO 语句
    Parameters
    ----------
    excel_path : str
        Excel 文件路径
    table_name : str
        需要写入的表名

    Returns
    -------
    str
        返回 SQL 的 INSERT INTO 语句
    """
    # 读取 Excel 文件
    df: pd.DataFrame = pd.read_excel(excel_path)

    # 生成字段名列表
    columns = list(df.columns)
    columns_str = ", ".join(columns)

    # 生成 SQL 语句
    data_list = []
    for _, row in df.iterrows():
        data_item = [f"\"{row[column]}\"" for column in columns]
        data_str = ", ".join(data_item)
        data_list.append(f"({data_str})")
    data_list_str = ",\n".join(data_list)

    return (f"INSERT INTO {table_name} ({columns_str}) \n"  f"VALUES \n"  f"{data_list_str};")


def main():
    insert_sql = generate_insert_sql(
        "D:/workspace/github/learning_python/com/roboslyq/python/tools/sql/insert-test.xlsx", "tuser")
    print(insert_sql)


if __name__ == '__main__':
    main()
