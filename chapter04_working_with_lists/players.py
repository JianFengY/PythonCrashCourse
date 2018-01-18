# -*- coding: utf-8 -*-
'''
Created on 2018年1月18日

@author: Jeff Yang
'''

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # 切片，切除索引从0开始，到2为止的元素
print(players[:4])  # 默认从索引0开始，到索引为3的元素
print(players[2:])  # 从索引2开始，到列表最后
print(players[-3:])  # 从倒数第三个元素开始，到末尾

print("\nHere are the first three players on the team:")
for player in players[:3]:  # 切片也可以遍历
    print(player.title())

# 另外，与列表类似，字符串和元组也有切片的操作
string = "test slice"
print("\n" + string[5:])
