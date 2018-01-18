# -*- coding: utf-8 -*-
'''
Created on 2018年1月18日

@author: Jeff Yang
'''

motorcyles = ['honda', 'yamaha', 'suzuki']
print(motorcyles)

motorcyles[0] = 'ducati'  # 直接对元素进行赋值可以修改列表元素
print(motorcyles)

motorcyles.append('honda')  # append()方法在列表最后添加一个元素
print(motorcyles)

motorcyles.insert(1, 'honda')  # 在索引为1的地方添加元素，后面的元素后移一位
print(motorcyles)

del motorcyles[1]  # del语句删除指定索引位置的元素，使用del删除后，就无法访问该元素了
print(motorcyles)

popped_motorcycles = motorcyles.pop()  # pop()方法删除最后一个元素，并返回该元素的值
print(popped_motorcycles)
print(motorcyles)

first_motorcycles = motorcyles.pop(0)  # pop()也可以删除指定索引位置的元素
print(first_motorcycles.title())
# 删除元素并且不需要再使用它可以使用del语句；删除后还需继续使用该元素就用pop()方法

print(motorcyles)  # ['yamaha', 'suzuki']
motorcyles.remove("yamaha")  # remove()根据元素值删除元素，若列表里出现了多个该值，则只删除第一个
print(motorcyles)
