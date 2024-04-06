# -*- coding: utf-8 -*-
import datetime
import os

# 输入目录路径
input_dir = 'C:\\Users\\Administrator\\Desktop\\demo\\'

# 获取当前日期和时间
now = datetime.datetime.now()

# 创建输出文件名
output_file = now.strftime("%Y%m%d%H%M%S") + '_binlog_sql.txt'

# 打开输出文件
with open(output_file, 'w') as file_out:
   # 遍历 binsql 目录下的所有 .sql 文件
   for filename in os.listdir(input_dir):
       if filename.endswith('.sql'):
           input_file = os.path.join(input_dir, filename)
           print(f"正在处理文件: {input_file}")

           # 打开输入文件
           with open(input_file, 'r', encoding='gbk', errors='ignore') as file_in:
               # 逐行读取输入文件
               for line in file_in:
                   # 如果行包含 '.',则写入输出文件
                   if line.startswith('### ') and '`.`' in line:
                       file_out.write(line)

print(f"提取完成。结果保存在 {output_file} 文件中。")