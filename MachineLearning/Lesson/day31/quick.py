#!/usr/bin/python
# author Yu
# 2023年06月24日
import sys
import os
import re

my_list = []


def recursion_dir(dir, width):
    file_list = os.listdir(dir)
    for file in file_list:
        data = re.search(r'.py$|.ipynb$', file)
        # 使用正则表达式，在空格前面加上反斜杠
        # file = re.sub(r'\s', r'\ ', file)
        path = os.path.join(dir, file)  # 拼接路径
        if data:  # 提取出.py文件
            my_list.append(path)  # 拼接后的路径添加到列表中
        if os.path.isdir(path):
            recursion_dir(path, width + 4)


recursion_dir('', 0)
name = 'day' + sys.argv[1] + '_龙哥.tar.gz '  # 拼名字
# os.system是Python调用bash shell的函数
print(name)
print(my_list)
os.system('tar czf ' + name + " ".join(my_list))  # 压缩
str_scp = 'scp ' + name + ' python10@42.192.117.114:~/day' + sys.argv[1]
os.system(str_scp)
print('提交成功')
