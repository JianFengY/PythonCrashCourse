# -*- coding: utf-8 -*-
'''
Created on 2018年1月18日

@author: Jeff Yang
'''

name = "aDa loVelace"
print(name.title())  # 让每个单词首字母大写，其他字母小写
print(name.upper())  # 全部字母大写
print(name.lower() + "\n")  # 全部字母小写
print(name * 2)  # 输出两次name变量的值
name2 = name.replace("loVe", "hate")  # 字符串替换
print(name2)
print(name.find('e'))  # 查找第一次出现e的位置，找不到返回-1
print(name.index('e'))  # 查找第一次出现e的位置，找不到会报错
print(name.count('ce'))  # 计算某字符或字符串出现的次数

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name  # 字符串拼接
message = "Hello," + full_name.title() + "!"
print("\t" + message + "\n")  # \t为制表符,\n为换行符

favorite_language = "  python   "
print(favorite_language.rstrip())  # 删除字符串右侧的空白字符
favorite_language = "****python*****"
print(favorite_language.lstrip("*"))  # 删除字符串左边的*号
print(favorite_language.strip("*"))  # 删除字符串两边的*号
print(favorite_language + "\n")  # 这种删除是暂时的，要永久删除，就将删除结果复制到原来变量中

message = "One of Python's strengths is its diverse community."
print(message)  # 正确度使用单引号和双引号，避免报错
