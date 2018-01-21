# -*- coding: utf-8 -*-
'''
Created on 2018年1月21日

@author: Jeff Yang
'''

# 第二个参数是模式实参，'w'-写入模式，'r'-读取模式，'a'-附加模式，'r+'-能读取和写入，省略参数则默认'r'
# 如果写入的文件不存在，open()函数将自动创建，'w'模式打开时，如果文件已存在，python将清空该文件
# write()函数写入文件，注意：python只能写入字符串，要存储数值，只能先使用str()转换为字符串
filename = 'programming.txt'
with open(filename, 'a') as file_object:
#     file_object.write("I love programming.\n")
#     file_object.write("I love creating new games.\n")
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")