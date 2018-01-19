# -*- coding: utf-8 -*-
'''
Created on 2018年1月19日

@author: Jeff Yang
'''

user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }
# key,value存储键和值，可以使用任何名称
# items()方法返回一个键值对列表
# 注意，即便是遍历，返回顺序也可能与存储顺序不同
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
