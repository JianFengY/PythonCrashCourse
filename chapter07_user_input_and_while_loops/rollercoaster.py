# -*- coding: utf-8 -*-
'''
Created on 2018年1月19日

@author: Jeff Yang
'''

height = input("How tall are you, in inches? ")
height = int(height)  # input()返回的是字符串，用int()转换为整型
# 而在python2中，非数字类型可以和数字类型比较，非数字类型>数字类型
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
