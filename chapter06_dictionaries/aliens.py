# -*- coding: utf-8 -*-
'''
Created on 2018年1月19日

@author: Jeff Yang
'''

alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':10}
alien_2 = {'color':'red', 'points':15}
aliens = [alien_0, alien_1, alien_2]  # 嵌套，可以在列表中嵌套字典，字典中嵌套列表甚至字典中嵌套字典
for alien in aliens:
    print(alien)

print("\n")
aliens = []
for alien_number in range (30):  # 创建30个
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:  # 修改前3个
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['poins'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[:5]:  # 使用切片显示前5个，索引0到4
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))
