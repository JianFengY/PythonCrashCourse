# -*- coding: utf-8 -*-
'''
Created on 2018年1月21日

@author: Jeff Yang
'''
# 单元测试
# 文件不要命名为unittest.py
import unittest
from name_function import get_formatted_name

# unittest模块中常用的断言方法：
# ==============================================
# assertEqual(a, b)       核实a == b
# assertNotEqual(a, b)    核实a != b
# assertTrue(x)           核实x为True
# assertFalse(x)          核实x为False
# assertIn(item, list)    核实item在list中
# assertNotIn(item, list) 核实item不在list中
# =============================================


# 可以随便命名，但最好看起来与要测试的类有关，并包含Test字样，而且要继承unittest.TestCase类，
class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    
    # 测试的方法名必须以'test_'开头！
    # 运行这个文件时，'test_'开头的方法都将自动运行
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        # 断言方法
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_middle_name(self):  # 方法名可以很长，所以要尽量描述清楚
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()  # 让python运行这个文件中的测试
# 测试通过打印一个句点‘.’ 测试引发错误(ERROR)打印一个‘E’ 测试导致断言失败(FAIL)打印一个‘F’

# 结果：
# ..    （表示有两个测试通过了）
# ----------------------------------------------------------------------
# Ran 2 test in 0.000s （用了0.000s运行了两个测试用例）
# 
# OK    （表示所有单元测试都通过了）

# 测试未通过示例：
# E    （有一个单元测试导致了错误）
# ======================================================================
# ERROR: test_first_last_name (__main__.NamesTestCase)    （错误的地方）
# 能够正确地处理像Janis Joplin这样的姓名吗？
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "D:\Program Files\eclipse\workspace\PythonCrashCourse\chapter11_testing_your_code\test_name_function.py", line 20, in test_first_last_name
#     formatted_name = get_formatted_name('janis', 'joplin')
# TypeError: get_formatted_name() missing 1 required positional argument: 'last'
# 
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s
# 
# FAILED (errors=1)    （测试未通过，因为有一个错误）

# 测试未通过时，不要修改测试，而应尝试修复代码
