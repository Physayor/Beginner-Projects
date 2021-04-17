# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 02:22:09 2021

@author: USER
"""
import copy

first_variable = {}
second_variable = dict()

fruit_basket = {
    "orange": 40,
    "apple": {"bad": 20, "good": 10},
    "pineapple": 5,
    "watermelon": 2
    }

print(type(first_variable))
print(type(second_variable))
print(isinstance(fruit_basket, dict))
print(fruit_basket)

# mangoes = fruit_basket["mangoes"]  # key error
mangoes = fruit_basket.get('', 0)
print("We have {} mangoes".format(mangoes))

# fruit_basket.pop("pineapple")
# print(fruit_basket)

new_fruit_basket = fruit_basket
# print(id(fruit_basket))
# print(id(new_fruit_basket))

# ".copy" returns the same thing as fruit basket even after altering only fruit basket 
new_fruit_basket = fruit_basket.copy()
# print(id(fruit_basket))
# print(id(new_fruit_basket))

print(fruit_basket)
print(new_fruit_basket)
print("===================================================")

# "copy.deepcopy" returns the same thing as the original fruit basket as the alteration
#  dosen't affect it
new_fruit_basket = copy.deepcopy(fruit_basket)
print(fruit_basket)
print(new_fruit_basket)
print("===================================================")

fruit_basket["apple"]["bad"] = 15
print(fruit_basket)
print(new_fruit_basket)










