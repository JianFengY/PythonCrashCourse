# -*- coding: utf-8 -*-
'''
Created on 2018年1月20日

@author: Jeff Yang
'''

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# for循环中不应该修改列表，否则将导致难以跟踪元素，要遍历时修改元素，可以用while循环
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())