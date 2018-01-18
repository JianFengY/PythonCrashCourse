# -*- coding: utf-8 -*-
'''
Created on 2018年1月18日

@author: Jeff Yang
'''

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # 按字母顺序永久性排序，sort()方法没有返回值
print(cars)

cars.sort(reverse=True)  # 按字母顺序逆序排序
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars, reverse=True))  # 函数sorted()对列表进行临时排序注意不是cars.sorted()!
print("Here is the original list again:")
print(cars)
print("\n")

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()  # 方法reverse()反转整个列表，没有返回值，也是永久修改顺序，再调用一次则恢复顺序
print(cars)

print(len(cars))  # 获取列表长度
