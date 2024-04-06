# -*- coding: utf-8 -*-
import re
# step-1生成的结果文件
output_file = '20240406191709_binlog_sql.txt'
# 用于提取库名和表名的正则表达式
pattern = r'`(\w+)`\.`(\w+)`'

# 存储库名和表名的字典
database_counts = {}
table_counts = {}

# 读取输入文件
with open(output_file, 'r', encoding='utf-8') as file:
   content = file.read()

# 使用正则表达式查找所有匹配项
matches = re.findall(pattern, content)

# 统计库的次数和表的次数
for match in matches:
   database, table = match

   # 统计库的次数
   if database in database_counts:
       database_counts[database] += 1
   else:
       database_counts[database] = 1

   # 统计表的次数,将库名和表名组合为键
   table_key = f"{database}.{table}"
   if table_key in table_counts:
       table_counts[table_key] += 1
   else:
       table_counts[table_key] = 1

# 打印结果
# 对database_counts的count求和
database_total = sum(database_counts.values())
print(f"0404 16:27-0405 16:27\nSQL执行次总次数: {database_total*93:,}")
print(f"\n每秒执行SQL次数: {database_total*93/24/3600:,}")
print("SQL执行次数-库:")
for database, count in sorted(database_counts.items(), key=lambda x: x[1], reverse=True):
   print(f"{database}: {count*4:,}")


print("\nSQL执行次数-表:")
for table_key, count in sorted(table_counts.items(), key=lambda x: x[1], reverse=True):
   print(f"{table_key}: {count*4:,}")