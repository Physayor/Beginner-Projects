# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 03:44:38 2021

@author: USER
"""

import random

random_number = random.randint(0, 20)
guess_number = input("Enter your guess number: ")
guess_number = int(guess_number)

while random_number != guess_number:
    if random_number > guess_number:
        print("Your guess is lesser than random number")
    else:
        print("Your guess is higher than random number")
    guess_number = input("Enter your guess number: ")
    guess_number = int(guess_number)
print("You guessed right")
