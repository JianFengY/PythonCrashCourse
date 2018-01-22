# -*- coding: utf-8 -*-
'''
Created on 2018年1月21日

@author: Jeff Yang
'''

"""一组可用于表示电动汽车的类"""

from chapter09_classes.car import Car  # 导入父类Car

# 创建子类时，父类必须包含在当前文件中，且位于子类前面，import导入也可以
# 定义子类时，括号内必须指定父类
# 子类可以根据需要重写父类的方法


class Battery():
    """一次模拟电动车电瓶的尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")  
        
    def get_range(self):
        """打印一条消息指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):  # __init__()方法要接收创建Carar实例所需的信息
        # super()方法帮助将父类和子类联系起来，这行代码调用父类的方法__init__()，让ElectricCar实例包含父类的所有属性
        super().__init__(make, model, year)
#         self.battery_size = 70  # 带初始值的新属性，根据ElectricCar创建的实例有这个属性，而Car没有
        self.battery = Battery()  # 创建一个Battery实例，现在每个ElectricCar实例都包含一个Battery实例
