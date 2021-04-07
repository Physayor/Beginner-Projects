# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 08:36:58 2021

@author: USER
"""

number = input("please enter your number: ")
number = int(number)

if number % 6 == 0:
    print("The number is divisible by 2 and 3")
elif number % 2 == 0:
    print("The number is a multiple of 2")
elif number % 3 == 0:
    print("The number is a multiple of 3")
else:
    print("The number is not divisible by 2 or 3")
