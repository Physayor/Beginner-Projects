# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 15:09:11 2021

@author: USER
"""

import datetime
user = input('What is your username? \n')
allowedUsers = ['Seyi', 'Mike', 'Love']
allowedPassword = ['passSeyi','passMike','passLove']
now = datetime.datetime.now()
if(user in allowedUsers):
        password = input('Your password is? \n')
        userId = allowedUsers.index(user)
        balance = 100000
        if(password == allowedPassword[userId]):
                print('Welcome %s' % user + ' ' + 'and you logged-in' + ' ' + now.strftime('%Y-%m-%d %H:%M:%S'))
                print('Your balance is %s' % balance)
                print('These are the available options:')
                print('1. Withdrawal')
        print('2. Cash Deposit')
                print('3. Complaint')
        selectedOption = int(input('Please select an option \n'))
                if(selectedOption == 1):
                    print('You selected 1')
                withdrawal = (input('How much would you like to withdraw? \n'))
                        if(withdrawal > balance):
                                print('Insufficient balance')
                        else:
                                print('Take your cash')
                elif(selectedOption == 2):
                        print('You selected 2')
                        deposit = int(input('How much would you like to deposit? \n'))
                        currentBalance = balance + deposit
                        print('Your current balance is %s' % currentBalance)
                elif(selectedOption == 3):
                        print('You selected 3')
                        Complaint = input('What issue will you like to report? \n')
                        print('Thanks for contacting us.')
        else:
                print('Error in password.')
else:
        print('Name not found')