# -*- coding: utf-8 -*-
'''
Created on 2018年1月19日

@author: Jeff Yang
'''

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "  # +=在prompt后面加一句话

name = input(prompt)
print("\nHello, " + name + "!")
