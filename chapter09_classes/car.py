# -*- coding: utf-8 -*-
'''
Created on 2018年1月20日

@author: Jeff Yang
'''

"""一个可用于表示汽车的类"""  # 模块级文档字符串，简要描述模块的内容，应为自己创建的每个模块编写文档字符串


class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):  # 无需odometer_reading
        """初始化描述汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 指定初始值，这样就无需提供初始值的形参
    
    def get_descriptive_name(self):
        """返回整洁的汽车信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):  # 使用方法修改属性值
        """
                        将里程表读数设置为指定的值
                        禁止将里程表回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles
