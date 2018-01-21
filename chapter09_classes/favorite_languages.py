# -*- coding: utf-8 -*-
'''
Created on 2018年1月21日

@author: Jeff Yang
'''

# python标准库是一组模块，安装的python里都包含它
from collections import OrderedDict  # 有序字典类，在将信息关联起来的同时保留了原来的顺序

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + 
        language.title() + ".")
