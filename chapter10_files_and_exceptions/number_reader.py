# -*- coding: utf-8 -*-
'''
Created on 2018年1月21日

@author: Jeff Yang
'''

import json

filename = 'numbers.json'

with open(filename) as file_object:
    # json.load()读取json数据
    numbers = json.load(file_object)
    
print(numbers)