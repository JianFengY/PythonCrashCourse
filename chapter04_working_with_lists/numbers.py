# -*- coding: utf-8 -*-
'''
Created on 2018年1月18日

@author: Jeff Yang
'''

for value in range(1, 5):  # 表示从1开始，到4位置
    # 默认情况下，range()起始值是0，rangr(5)范围为0到4
    print(value)

numbers = list(range(1, 6))  # 使用函数list()将range()的结果直接转换为列表
print(numbers)

even_numbers = list(range(2, 11, 2))  # 第三个参数2表示间隔，即从2开始，不断加2
print(even_numbers)

squares = []
for value in range(1, 11):  # 循环创建整数1到10的平方的列表
    squares.append(value ** 2)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))  # 找出最小值
print(max(digits))  # 最大值
print(sum(digits))  # 求和

squares = [value ** 2 for value in range(1, 11)]
# 列表解析，这里的for没有冒号，for后面还可以嵌套如if判断的语句
print(squares)
