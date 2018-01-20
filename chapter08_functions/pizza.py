# -*- coding: utf-8 -*-
'''
Created on 2018年1月20日

@author: Jeff Yang
'''


# 使用*号会创建一个空的名为toppings的元组，并将接收的所有值存到该元组中
# 如果函数要接收不同类型的实参，必须在定义中将接纳任意数量实参的形参放在最后
def make_pizza(size, *toppings):
    """打印顾客点的所有配料"""
    print("\nMaking a " + str(size) + 
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
