# -*- coding: utf-8 -*-
'''
Created on 2018年1月21日

@author: Jeff Yang
'''

from car import Car  # 导入Car类，依然可以使用其所有功能

# 我们可以在一个py文件即一个模块例存储多个类
# 如：可以通过from car import Car1, Car2导入Car1和Car2两个类
# 还可以导入整个模块 import car，然后通过句点方式访问需要的类，如car.Car1(),car.Car2()
# 也可以通过from module_name import * 导入所有类，当然，和导入函数一样，这也是不推荐的

my_new_car = Car('audi', 'a4', 2016)  # 创建Car实例
print(my_new_car.get_descriptive_name())  # 调用方法
my_new_car.odometer_reading = 23  # 通过实例访问并直接修改属性值
my_new_car.update_odometer(23)  # 调用方法修改属性值
my_new_car.read_odometer()
 
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
