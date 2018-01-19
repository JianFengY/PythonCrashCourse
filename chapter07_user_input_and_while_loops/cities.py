# -*- coding: utf-8 -*-
'''
Created on 2018年1月19日

@author: Jeff Yang
'''

prompt = "\nPlease tell me a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break  # break立即退出循环，不执行之后的内容
    else:
        print("I'd love to go to " + city.title() + "!")
