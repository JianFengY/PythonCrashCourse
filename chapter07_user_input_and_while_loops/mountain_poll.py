# -*- coding: utf-8 -*-
'''
Created on 2018年1月20日

@author: Jeff Yang
'''

responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    responses[name] = response  # 添加键值对
    
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
        
print("\n--- Poll Results ---")
for name, response in responses.items():  # 遍历字典
    print(name + " would like to climb " + response + ".")
