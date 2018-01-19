# -*- coding: utf-8 -*-
'''
Created on 2018年1月19日

@author: Jeff Yang
'''

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:  # python不要求必须有else代码块，如果知道最终测试条件，应考虑使用elif代码块代替else使代码比较清晰
    price = 5
print("Your admission cost is $" + str(price) + ".")
