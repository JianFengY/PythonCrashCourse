# -*- coding: utf-8 -*-
'''
Created on 2018年1月21日

@author: Jeff Yang
'''

import json

# # 如果以前存储了用户名，就加载它
# # 否则，就提示用户输入用户名并存储它
# 
# filename = 'username.json'
# try:
#     with open(filename) as f_obj:
#         username = json.load(f_obj)
# except FileNotFoundError:
#     username = input("What is your name?")
#     with open(filename, 'w') as f_obj:
#         json.dump(username, f_obj)
#         print("We'll remember you when you come back, " + username + "!")
# else:
#     print("Welcome back, " + username + "!")

# 代码能够正确运行，但可以改进，将代码划分为一系列完成具体工作的函数，这样的过程称为重构。让代码更清晰、易于理解和扩展


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None  # 一种不错的做法，函数要么返回预期值，要么返回None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
