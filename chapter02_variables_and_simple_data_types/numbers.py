# -*- coding: utf-8 -*-
'''
Created on 2018年1月18日

@author: Jeff Yang
'''

print(2 ** 3)  # 2的3次方，python使用**表示乘方运算

print(0.2 + 0.1)  # 二进制和十进制的转换会造成小数位数不确定的问题

age = 23
message = "Happy " + str(age) + "rd Birthday!"  # 使用函数str()让非字符串数值表示为字符串，否则会报类型错误
print(message)

print(3 / 2)  # python3结果为1.5，而python2中，整数除法结果的小数部分会直接删除，结果会是1。需要确保至少有一个数为浮点数
