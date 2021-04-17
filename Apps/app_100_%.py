# -*- coding: utf-8 -*-.
"""
Created on Thu Apr  1 19:17:26 2021

@author: USER
"""

import sys
from datetime import datetime
# Requests users name
name = input("What is your Name?\n")
# Prepopulated list of allowed users
allowedUsers = ["Seyi", "Mike", "Love"]
# Passwords assigned to allowed users
allowedPasswords = ["passwordSeyi", "passwordMike", "passwordLove"]
# Evaluates is in the list of names
if name not in allowedUsers:
    sys.exit("Name not found, please try again")
# Indexes users input
userId = allowedUsers.index(name)
passwordCount = 0
# Checks for indexed users password in the allowed passwords
# While loop allows for only three trials on the user's...
# password using passwordCount
while True:
    password = input("Your Password:\n")
    if password != allowedPasswords[userId]:
        passwordCount += 1
        if passwordCount == 3:
            sys.exit("Password limit reached\nPlease try again later")
    else:
        break
# Assigns the local date and time to a variable
currentDateAndTime = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
# Prints the local date and time
print(f"\n{currentDateAndTime}\n\nWelcome {name},\nThese are the available options:")
# Displays options for user to select
print("1. Withdrawal\n2. Cash Deposit\n3. Lodge a Complaint\n")
# Requests input from user
userInput = int(input("Please select an option:\n"))
# Checks to user input and asks corresponding question
if userInput == 1:
    input("How much would you like to withdraw?\n")
    sys.exit("Please take your cash")
elif userInput == 2:
    deposit = input("How much would you like to deposit?\n")
    sys.exit(f"Current balance = {deposit}")
elif userInput == 3:
    complaint = input("What issue would you like to report?\n")
    sys.exit("Thank you for contacting us")
else:
    sys.exit("Invalid Option selected, please try again later")
