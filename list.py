# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 04:41:55 2021

@author: USER
"""

my_food_item_list = ["garri","peak milk","milo","golden morn","corn flakes","sugar"]

print(my_food_item_list)

item = my_food_item_list[1]

print(item)

last_item = my_food_item_list[-1]

print(last_item)

my_food_item_list[-2]="quacker oat"

print(my_food_item_list)

list_of_items = my_food_item_list[2:5]

print(list_of_items)

for i in range(6):
    print(my_food_item_list[i])

my_food_item_list.append("corn flakes")
for i in range(len(my_food_item_list)):
    print(my_food_item_list[i])
    
for item in my_food_item_list:
    print(item)