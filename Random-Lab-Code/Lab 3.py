# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 09:57:35 2018

@author: chris
"""
userNames = list()
while True:
    existing = input("Are you a new user? ")
    if existing == ("Yes") or existing == ("yes"):
        firstName = input("Please enter a first name ")
        lastName = input("Please enter a Last name ")
        userName = firstName[0] + lastName [:7]
        print ("Your username is "+ userName)
        userNames.append (userName)
    if existing == ("No") or existing == ("no"):
        userName = input("Enter your username ")
        if userName in userNames:
            print ("That username already exists")
        else:
            print ("That username is not added")