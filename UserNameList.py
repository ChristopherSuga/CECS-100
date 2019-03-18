# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 12:12:13 2018

@author: chris
"""
userNames = list()
while True:
    firstName = input("Please enter a first name or Done ")
    if firstName == ("Done"):
        break
    lastName = input("Please enter a Last name ")
    userName = firstName[0] + lastName [:7]
    print ("Your username is "+ userName)
    userNames.append (userName)
    userName = input("Enter your username ")
    if userName in userNames:
        print ("That username is added")
    if userName not in userNames:
        print ("That username is not added")
print (userNames)