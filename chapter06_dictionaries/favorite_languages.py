# -*- coding: utf-8 -*-
'''
Created on 2018年1月19日

@author: Jeff Yang
'''

favorite_languages = {
    'jen':'python',  # 缩进4个空格，末尾加逗号
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',  # 最后一个元素后面也可以加上逗号，为以后下一行键值对做准备
    }
# 长语句分行，注意缩进对齐和拼接符
print("Sarah's favorite language is " + 
      favorite_languages['sarah'].title() + 
      ".\n")

# 这里循环变量中使用name和language让代码更清晰
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + 
        language.title() + ".")

print("\n")
for name in favorite_languages.keys():  # 方法keys()返回包含所有键的一个列表，不需要值时很有用
    print(name.title())

print("\n")
for name in favorite_languages:  # 遍历时默认遍历所有的键，跟使用方法keys()结果一样
    print(name.title())

print("\n")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("  Hi " + name.title() + 
              ", I see your favorite language is " + 
              favorite_languages[name].title() + "!")

print("\n")
for name in sorted(favorite_languages.keys()):  # 使用sorted()按首字母顺序排序
    print(name.title() + ", thank you for taking the poll.")

print("\nThe following languages have been mentioned:")
# 类似的，values()方法返回所有值的列表
for language in set(favorite_languages.values()):  # 使用集合set可以去重，set与列表类似，但元素不会重复
    print(language.title())

# 注意嵌套的层级最好不要太多
print("\n")
favorite_languages = {
    'jen':['python', 'ruby'],
    'sarah':['c'],
    'edward':['ruby', 'go'],
    'phil':['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    print(name.title() + "'s favorite language " + 
          ("are: " if len(languages) > 1 else "is: "))  # 判断列表个数决定用is还是are
    for language in languages:
        print("\t" + language.title())
