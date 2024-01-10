# coding:utf-8
import shutil
import subprocess
import os
import traceback
import sys


def copy_files_from_list(file_list_path, destination_directory):
    """Copies files from list:根据清单复制文件"""
    with open(file_list_path, 'r') as listFile:
        source_file = listFile.readline()
        while source_file:
            source_file_name = os.path.basename(source_file)
            source_file_path = source_file.strip("\n")
            destination_file = destination_directory + "\\" + source_file_name.strip()
            try:
                shutil.copy(source_file_path, destination_file)
                print("复制文件: " + source_file + " -> " + destination_file)
            except IOError:
                traceback.print_exc()
            source_file = listFile.readline()


def compress_directory(directory_path, output_file):
    """Compresses:对文件进行打包压缩"""
    # 使用tar命令进行压缩打包
    subprocess.call(['tar', '-zcvf', output_file, directory_path])
    print("压缩打包目录: {} -> {}".format(directory_path, output_file))


def main():
    # 清单文件的路径
    file_list_path = 'file_list.txt'
    # 目标目录
    destination_directory = 'E:/workspace_python/github/learning_python/com/roboslyq/python/tools/target'
    # 复制文件到目标目录
    copy_files_from_list(file_list_path, destination_directory)
    # 需要压缩打包的目录
    directory_path = destination_directory
    # 压缩打包输出文件路径
    output_file = 'output.tar.gz'
    # 压缩打包目录
    compress_directory(directory_path, output_file)


if __name__ == '__main__':
    main()
