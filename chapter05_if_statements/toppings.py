# -*- coding: utf-8 -*-
'''
Created on 2018年1月19日

@author: Jeff Yang
'''

# PEP8对代码格式的建议：在诸如==、>=和<=等比较运算符两边各加一个空格

requested_toppings = ['mushrooms', 'extra cheese']
# 使用多个简单的if语句，不管前面的结果是不是True，后面的语句都会独立地执行测试
# 只想执行一个代码块就用if-elif-else结构，如果要运行多个代码块，就使用一系列独立if语句
if 'mushrooms' in requested_toppings:
    print("Add mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Add pepperoni.")
if 'extra cheese' in requested_toppings:  # 如果使用elif，这句就不会执行了
    print("Add extra cheese.")
print("Finished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
print("\n")
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("Finished making your pizza!")

requested_toppings = []
if requested_toppings:  # 判断列表是否为空
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
print("\n")
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:  # 判断点的配料是否在供应配料里
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("Finished making your pizza!")
