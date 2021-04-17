# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 09:49:47 2021

@author: USER
"""

counter = 5
while counter > 0:
    if counter == 3:
        counter -= 1
        continue
    print(counter)
    counter -= 1
print("The loop has ended")

counter = 8
while counter % 2 == 0:
    print(counter)
    counter /= 2

print("The loop has ended")
