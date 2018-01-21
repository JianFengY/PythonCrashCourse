# -*- coding: utf-8 -*-
'''
Created on 2018年1月21日

@author: Jeff Yang
'''

# print(5 / 0)  # 异常对象：ZeroDivisionError

# try-except代码块捕获异常
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by 0!")

# try-except-else代码块工作原理：
# python尝试执行try代码块中的代码，只有可能引发异常的代码才需要放在try语句中
# 仅在try成功执行才需要执行的代码放在else代码块中
# except代码块告诉python，如果尝试运行try代码块中的代码时发生指定的异常该怎么办

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    except ValueError:
        print("Please enter valid number!")
    else:  # 依赖于try代码块成功执行的代码都应该放在else代码块中
        print(answer)
