# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 19:08:29 2021

@author: USER
"""

numberList = [5, 7, 12, 9, -5, 10]
maxNumber = numberList[0]

for number in numberList:
    if number > maxNumber:
        maxNumber = number
print(maxNumber)

number_list = [3, 6, 1, 0, 20, 50, 2, -10, -50]
max_number = number_list[0]
max_number_index = 0
counter = 0

for i in range(len(number_list)):
    if number_list[i] > max_number:
        max_number = number_list[i]
        max_number_index = i

for number in number_list:
    if max_number == number:
        continue
    if max_number >= 2 * number:
        counter += 1
if counter == len(number_list) - 1:
    print(max_number_index)
else:
    print(-1)
