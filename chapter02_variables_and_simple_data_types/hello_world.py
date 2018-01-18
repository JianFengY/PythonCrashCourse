# -*- coding: utf-8 -*-
'''
Created on 2018年1月18日

@author: Jeff Yang
'''
# 符合标准python约定的文件名：使用小写字母和下划线，如 hello_world.py

# 变量名只能包含字母、数字和下划线
# 变量名不能包含空格，可使用下划线分隔其中的单词
# 不要用python关键字和内置函数名用作变量名，使用如class、def等关键字用作变量名时将报错，而使用内置函数名如print，将覆盖函数的行为
# 变量名应既简短又有描述性
# 慎用小写字母l和大写字母O，因为容易与数字1和0混淆
# 变量名建议使用小写字母
message = "Hello Python World!"
print(message)

# 程序中可以随时修改变量值，python始终记录变量的最新值
message = "Hello Python Crash Course World!"
print(message)
