# -*- coding: utf-8 -*-
'''
Created on 2018年1月20日

@author: Jeff Yang
'''

# 类名应采取驼峰命名法，即每个单词首字母大写，不使用下划线，而实例名和模块名则使用小写字母和下划线
# 对于每个类，都应该紧跟在类定义后面包含一个文档字符串，描述类的功能，每个模块也应包含一个文档字符串
# 在类中，使用一个空行来分隔方法；而在模块中，使用两个空行来分隔类；另外，若在程序或模块中有多个函数，函数之间也可以用两个空行分隔
# 需要同时导入标准库的模块和自己编写的模块时，先import标准库模块，再加一个空行，然后再import自己编写的模块


class Dog():  # 首字母大写
    """一次模拟小狗的简单尝试"""  # 文档字符串

    # 类中的函数称为方法
    # __init__()是一个特殊的方法，每当你创建新实例时，python都会自动运行它
    # 这个方法开头末尾都有两个下划线，这是一种约定，旨在避免python默认方法与普通方法名发生冲突
    # 方法的self参数必不可少，且必须在其他参数之前。
    # python调用__init__()方法创建Dog实例时，将自动传入self实参，不需要手动传入
    # 每个与类相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，让实例能访问类中的属性和方法
    def __init__(self, name, age):
        """初始化属性name和age"""
        # 两个变量都有self，以self为前缀的变量都可供类中的所有方法使用
        # 可以通过实例访问的变量称为属性
        self.name = name  # 把传入的name存储在与当前创建的实例关联的name中
        self.age = age
    
    def sit(self):
        """模拟小狗下蹲"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)  # 创建实例
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")  # my_dog.name通过实例访问属性
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()  # 调用方法

print("\nMy dog's name is " + your_dog.name.title() + ".")
print("My dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
