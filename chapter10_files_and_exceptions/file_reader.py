# -*- coding: utf-8 -*-
'''
Created on 2018年1月21日

@author: Jeff Yang
'''

# open()用于打开文件，接受文件名称为参数，返回一个表示所打开文件的对象，存在file_object变量中
# 关键字with使python在不需要使用该文件后自动将其关闭，避免出现未关闭或过早关闭文件的情况
# 也可以调用open()和close()来打开关闭文件，但如果程序出错导致close()未执行，文件将不会关闭
# 如果文件不在当前目录下，可以指定相对路径或绝对路径，如with open('test\pi_digits.txt') as file_object:
# 在windows系统中，文件系统中使用反斜杠\，linux和OS X中使用斜杠/
# 相对路径：相对当前目录的路径，“..”表示上层目录（父目录），“.”表示当前目录
# 绝对路径：从盘符开始的完整路径
# 读取文本文件时，所有文本都会被解读成字符串，要把数字当数值要使用函数int()或float()转化为整型或浮点型

file_name = 'pi_digits.txt'  # 把文件名存在一个变量里，是比较常见的做法
with open(file_name) as file_object:
    # read()方法读取文件的全部内容，并作为一个字符串存储在变量contents中
    contents = file_object.read()
    print(contents.rstrip())
    # 打印出来的内容在末尾会多一个空行，因为read()到达文件末尾时返回一个字符串，显示出来就是一个空行，使用rstrip()方法删除

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())
        # 文件每一行都有一个换行符，而print语句也会加一个换行符，所以要去掉一个

with open(file_name) as file_object:
    lines = file_object.readlines()  # readlines()方法读出每一行并保存在一个列表中
for line in lines:
        print(line.rstrip())
