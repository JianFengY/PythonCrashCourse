# -*- coding: utf-8 -*-
'''
Created on 2018年1月19日

@author: Jeff Yang
'''

banned_users = ['andrew', 'caralina', 'david']
user = 'marie'

print("Yes" if user in banned_users else "No")  # in检查特定值是否包含在列表中

if user not in banned_users:  # not in检查特定值是否不包含在列表中
    print(user.title() + ", you can post a response if you wish.")

# 类似三目运算符的用法，找出较大的数
a, b = 1, 2  
print(a if a > b else b)
print(a > b and a or b)
