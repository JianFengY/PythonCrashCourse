# -*- coding: utf-8 -*-
'''
Created on 2018年1月21日

@author: Jeff Yang
'''

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'  # json文件存储json格式的数据
with open(filename, 'w') as file_object:
    # json.dump()接受两个参数，要存储的数据和用于存储数据的文件对象
    json.dump(numbers, file_object)
