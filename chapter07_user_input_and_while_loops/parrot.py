# -*- coding: utf-8 -*-
'''
Created on 2018年1月19日

@author: Jeff Yang
'''

# python2中用raw_input()，它接收输入转换成string返回，输入数字也会当成string
# python2中input()原理上是raw_input()调用eval()函数，输入字符串要用引号引起
# python3中raw_input()和input()进行了整合,仅保留了input()函数，其接收任意输入并返回字符串类型。
# eval()：把字符串当成有效的python表达式求值并计算结果
# repr()：把变量和表达式转换成字符串表示

# message = input("Tell me something, and I will repeat it back to you:")
# print(eval(message))

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':  # 只要没有输入quit，循环就会一直继续下去
#     message = input(prompt)
#     if message != 'quit':  # 输入quit的话不会输出
#         print(message)
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False  # 注意要设定结束标志，避免无限循环
    else:
        print(message)
