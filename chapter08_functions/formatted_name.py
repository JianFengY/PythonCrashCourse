# -*- coding: utf-8 -*-
'''
Created on 2018年1月20日

@author: Jeff Yang
'''


def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:  # python将非空字符串解读为True
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()  # 返回值


musician = get_formatted_name('jimi', 'hendrix')  # musician用于接收函数的返回值
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at any time to quit)")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last_name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("Hello, " + formatted_name + "!")
