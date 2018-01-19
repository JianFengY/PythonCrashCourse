# -*- coding: utf-8 -*-
'''
Created on 2018年1月19日

@author: Jeff Yang
'''

users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
        },
    }
# 这里user_info也是个字典，并且每位用户的字典结构都相同，这样处理起来更容易
for username, user_info in users.items():
    print("\nUsername:" + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
