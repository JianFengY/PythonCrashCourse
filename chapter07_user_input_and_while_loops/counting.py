# -*- coding: utf-8 -*-
'''
Created on 2018年1月19日

@author: Jeff Yang
'''

current_number = 1
while current_number <= 5:  # 注意冒号
    print(current_number)
    current_number += 1

print("\n")
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue  # continue忽略余下的代码，直接进行下一次循环
    print(current_number)
