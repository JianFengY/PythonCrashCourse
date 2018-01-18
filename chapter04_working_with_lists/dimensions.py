# -*- coding: utf-8 -*-
'''
Created on 2018年1月19日

@author: Jeff Yang
'''

# 列表是可以修改的，而元组的值是不可变的
# 元组使用括号()标识
dimensions = (200, 50)
print(dimensions[0])  # 访问元组元素和列表相似
print(dimensions[1])

# 单元素元组要加一个逗号避免歧义，如dimensions = (200,)
dimensions = (200)
print(type(dimensions))  # <class 'int'>

# dimensions[0] = 250 修改元组的值会报错

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
print("Modified dimensions:")
dimensions = (400, 100)  # 虽然不能修改元组的元素，但可以给存储元组的变量重新赋值
for dimension in dimensions:
    print(dimension)
    
my_tuple = (1, [2, 3], 4, 5)
my_tuple[1][0] = 3  # 元组本身的指向不可变，若指向list，就不能改成指向其他对象，但list本身是可变的
print(my_tuple)  # (1, [3, 3], 4, 5)
