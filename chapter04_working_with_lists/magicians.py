# -*- coding: utf-8 -*-
'''
Created on 2018年1月18日

@author: Jeff Yang
'''

magicians = ['alice', 'david', 'carolina']
for magician in magicians:  # for循环遍历列表，这种单复数的命名有助于处理的是列表还是单个元素
    print(magician.title() + ", that was a good trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    # 相同缩进视为代码块，缩进为4个空格，若上面这行没有缩进，magician最后的值为carolina，只会显示这一条，但不会报错
print("Thank you, everyone. That was a great magic show.")
