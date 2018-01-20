# -*- coding: utf-8 -*-
'''
Created on 2018年1月20日

@author: Jeff Yang
'''


# 函数的理念：每个函数都应只负责一项具体的工作
def print_models(unprinted_designs, completed_models):
    """
            模拟打印每个设计，直到没有未打印的设计
            打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
    
        # 模拟打印的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)

    
def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)
# print(unprinted_designs)  # 空列表

# 使用列表复制unprinted_designs[:]，这样pop()改变的只是副本，可以用于保留原始列表的数据
# 除非有充分理由，否则还是应该传递原始列表，避免花时间和内存创建副本
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)  # 原来的内容还在
