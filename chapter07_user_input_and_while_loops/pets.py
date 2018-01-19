# -*- coding: utf-8 -*-
'''
Created on 2018年1月20日

@author: Jeff Yang
'''

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')  # remove()删除第一个遇到的元素，循环删除所有cat元素
print(pets)
