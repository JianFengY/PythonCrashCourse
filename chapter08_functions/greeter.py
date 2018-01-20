# -*- coding: utf-8 -*-
'''
Created on 2018年1月20日

@author: Jeff Yang
'''

# 函数（Function）：直接定义，不与其他东西有关系，只需要相关参数
# 方法（Method）：类里面定义的函数就是方法，与某个对象有关联


# 定义一个函数，函数名+括号，括号里面放参数，后接冒号
def greet_user(username):  # 这里username是一个形参，是函数所需的信息
    """显示简单的问候语"""  # 文档字符串(docstring)，用于生成有关程序中函数的文档
    print("Hello, " + username.title() + "!")


greet_user('jesse')  # 调用函数，这里的jesse是一个实参，是调用函数时给函数传递的信息，值被存储在形参username中
