# -*- coding: utf-8 -*-
'''
Created on 2018年1月21日

@author: Jeff Yang
'''

filename = 'alice.txt'  # 当前目录没有这个文件就会发生FileNotFoundError异常
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError as e:
    msg = "Sorry, the file '" + filename + "' does not exist."
    print(msg)
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
