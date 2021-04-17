# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 22:11:39 2021

@author: USER
"""

name = input("What is your name? \n")
acceptedName = ["Seyi", "Femi", "Love"]
acceptedPassword = ["passwordSeyi", "passwordFemi", "passwordLove"]

if name in acceptedName:
    password = input("Input your password: \n")
    userId = acceptedName.index(name)

    if password == acceptedPassword[userId]:

        from datetime import datetime
        now = datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        print("\n>>", now)
        print("Welcome %s! \n" % name)

        print("These are the available options;")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Complaint")

        selectedOption = input("Please select an option: ")
        selectedOption = int(selectedOption)

        if selectedOption == 1:
            input("How much would you like to withdraw?: #")
            print("Take your cash!")

        elif selectedOption == 2:
            deposit = input("How much would you like to deposit?: #")
            currentBalance = deposit
            currentBalance = int(currentBalance)
            print("Your Current Balance is %s" % currentBalance)

        elif selectedOption == 3:
            input("What issue will you like to report?: ")
            print("Thank you for contacting us!")

        else:
            print("Invalid Option, please select a valid option")

    else:
        print("Incorrect Password, please try again!")

else:
    print("Wrong username, please try again!")
