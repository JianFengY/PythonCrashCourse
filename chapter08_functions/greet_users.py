# -*- coding: utf-8 -*-
'''
Created on 2018年1月20日

@author: Jeff Yang
'''

def greet_users(names):
    """向列表中的每位用户发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)