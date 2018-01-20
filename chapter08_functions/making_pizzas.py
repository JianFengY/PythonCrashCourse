# -*- coding: utf-8 -*-
'''
Created on 2018年1月20日

@author: Jeff Yang
'''
import pizza  # 导入pizza模块，让python打开pizza.py文件，并将所有代码复制到当前程序中，可以使用其中定义的函数

# 使用import module_name导入模块，可以通过module_name.fuction_name()使用函数
# from module_name import function_1, function_2, function_3导入模块中的函数
# 使用from pizza import make_pizza的话就可以直接make_pizza(16, 'pepperoni')使用函数
# from module_name import * 导入模块里的所有函数，也可以直接使用函数，但最好不要这样做，如果与你的函数同名会产生覆盖
# 最佳做法是，要么只导入需要使用的函数，要么导入整个模块使用句点表示让代码更清晰

# 编写函数时应指定描述性名称，且使用小写字母和下划线
# 每个函数都应该包含简要的描述功能的注释，注释紧跟函数定义后面，并采用文档字符串格式（三引号）
# 无论是定义还是调用，函数括号里的等号两边都不用空格
# 若函数定义过长，可以在函数定义左括号回车，在下一行按两次tab键，从而将形参列表和函数体分开
# def function_name(
#         parameter_0, parameter_1, parameter_2,
#         parameter_3, parameter_4, parameter_5,):
#     function body...
# 如果程序或模块包含多个函数，可使用两个空行将相邻的函数分开使代码更清晰
# 所有import语句都应该在文件开头，除非文件开头使用了注释来描述整个程序

# 可以使用as指定函数别名，如from pizza import make_pizza as mp，就可以mp(16, 'pepperoni')使用
# 也可以用as给模块指定别名，如import pizza as p，使用p.make_pizza(16, 'pepperoni')

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
