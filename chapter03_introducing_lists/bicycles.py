# -*- coding: utf-8 -*-
'''
Created on 2018年1月18日

@author: Jeff Yang
'''

# 使用方括号[]表示列表，并用逗号分隔元素
bicycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles[0].title())  # 使用索引访问元素，索引从0开始
print(bicycles[-1])  # 索引-1表示最后一个元素，-2表示倒数第二个，以此类推

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
