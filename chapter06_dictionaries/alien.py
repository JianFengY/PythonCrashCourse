# -*- coding: utf-8 -*-
'''
Created on 2018年1月19日

@author: Jeff Yang
'''

# 字典是一系列键值对，键与值之间用冒号分隔，键值对之间用逗号分隔
# 键必须是唯一的，而值不一定
# 键必须是不可变的，如字符串，数字或元组，而值可以是任何数据类型
alien_0 = {'color':'green', 'points':5}
print(alien_0['color'])  # 获取字典与键关联的值
print(alien_0['points'])

alien_0['x_position'] = 0  # 字典是动态结构，添加键值对只要指定字典名、方括号括起的键和相关联的值
alien_0['y_position'] = 25
print(alien_0)  # python不关心键值对的添加顺序，只关心键值的关联关系

alien_0 = {'color':'green'}
print("\nThe alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed':'medium'}
print("Original x-position:" + str(alien_0['x_position']))
# 根据速度向右移动外星人
if alien_0['speed'] == "slow":
    x_increment = 1
elif alien_0['speed'] == "medium":
    x_increment = 2
elif alien_0['speed'] == "fast":
    x_increment = 3
# 新位置
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position:" + str(alien_0['x_position']))

print("\n")
alien_0 = {'color':'green', 'points':5}
print(alien_0)
del alien_0['points']  # del语句将指定的键值对彻底删除，要指定字典名和键名
print(alien_0)

print("\n")
alien_0 = {'color':'green', 'points':5}
print(alien_0)
poped_item = alien_0.pop('color')  # pop()方法删除指定键值对并返回指定键的值
print(poped_item)
print(alien_0)

print("\n")
alien_0 = {'color':'green', 'points':5}
print(alien_0)
alien_0.clear()  # clear()方法删除整个字典元素，没有返回值
print(alien_0)
