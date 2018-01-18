# -*- coding: utf-8 -*-
'''
Created on 2018年1月18日

@author: Jeff Yang
'''
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # 利用切片复制列表
my_foods.append("cannoli")
friend_foods.append("ice cream")
print("My favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods  # 直接赋值两个变量指向的是同一个列表，修改一个，另一个也会改变
my_foods.append("cannoli")
friend_foods.append("ice cream")
print("\nMy favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)
