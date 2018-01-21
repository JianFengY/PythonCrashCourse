# -*- coding: utf-8 -*-
'''
Created on 2018年1月21日

@author: Jeff Yang
'''


def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError as e:
        pass  # pass语句让python什么都不做，发生异常不会traceback也没有任何输出
        # pass语句还充当占位符，他提醒你在程序中的某个地方什么都没有做，并且以后也许要在这里做些什么
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()  # 以空格拆分文件，并得到一个包含分好的所有部分的一个列表，虽然有些单词会包含标点
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:  # 一个文件找不到并不会影响下一个循环
    count_words(filename)
