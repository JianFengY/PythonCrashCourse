# -*- coding: utf-8 -*-
'''
Created on 2018年1月19日

@author: Jeff Yang
'''

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':  # 条件测试，注意python是大小写敏感的
        print(car.upper())
    else:
        print(car.title())

print("\n")
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)  # and表示“且”，同时为True才是True
print(age_0 >= 21 or age_1 >= 21)  # or表示“或”，只要其中一个为True就为True
