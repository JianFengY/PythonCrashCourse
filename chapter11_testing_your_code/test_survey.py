# -*- coding: utf-8 -*-
'''
Created on 2018年1月21日

@author: Jeff Yang
'''

import unittest
from chapter11_testing_your_code.survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    
    # python将先运行方法setUp()，再运行每个以'test_'开头的方法
    # 在setUp()方法里创建一系列实例并设置它们的属性，就能在每个测试方法里使用了这些事例
    def setUp(self):
        """创建一个调查对象和一组答案，供测试方法使用"""
        question = "What language did you first learn to speak?"
        # 这里变量名都包含self前缀，即存储在属性中，因此可以在这个类的任何地方使用
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    
    def test_store_single_response(self):
        """测试单个答案会被妥善储存"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善储存"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()
