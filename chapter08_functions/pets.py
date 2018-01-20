# -*- coding: utf-8 -*-
'''
Created on 2018年1月20日

@author: Jeff Yang
'''


# 注意，使用默认值时，要先列出没有默认值的形参，这样能正确解读位置实参
def describe_pet(pet_name, animal_type='dog'):  # animal_type设了默认值为dog
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('harry', 'hamster')  # python将按位置顺序将实参关联到形参中
describe_pet(animal_type='dog', pet_name='willie')  # 关键字实参，不用考虑顺序
describe_pet('willie')  # 由于有默认值，animal_type不传值就会使用默认值
