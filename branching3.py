# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 17:31:20 2021

@author: USER
"""

score=input("Enter the Score from 0-100: ")
score=int(score)

if score >=70 and score <=100:
    print("A")
elif score >=60 and score<70:
    print("B")
elif score >=50 and score<60:
    print("C")
elif score >=45 and score<50:
    print("D")
elif score >=40 and score<45:
    print("E")
elif score >=0 and score<40:
    print("F---You have failed this course, see you next year.")
else:
    print("Please input scores within the given range")
