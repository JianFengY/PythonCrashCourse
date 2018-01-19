# -*- coding: utf-8 -*-
'''
Created on 2018年1月19日

@author: Jeff Yang
'''

# 字典里嵌套列表
pizza = {
    'crust':'thick',
    'toppings':['mushrooms', 'extra cheess'],
    }
print("You ordered a " + pizza['crust'] + "-crust pizza " + 
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
