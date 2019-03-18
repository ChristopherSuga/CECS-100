# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 09:57:35 2018

@author: chris
"""
c= 3 #initializes a counter for the amount of tries left when logging in
userNames = list() #initializes an empty list for usernames
passwords = list()#initializes an empty list for passwords
while True:
    existing = input("Are you a new user? ") #asks if existing user
    if existing == ("Yes") or existing == ("yes"): #if input is yes
        while True:
            firstName = input("Please enter a first name ") #asks user for first name
            lastName = input("Please enter a Last name ")  #asks user for last name
            userName = firstName[0] + lastName [:7] #creates username based off of first+last name
            if userName in userNames: #check if username exists
                print ("That username already exists ") #prints if username exists
                while True:
                    userName = input("Enter a new username ") #asks for a new username
                    if userName in userNames: #check if username exists
                        continue
                    else:
                        print ("That username is not added") #prints if user doesn't exist
                        userNames.append(userName) #appends username to list
                        print ("Your username is "+ userName) #prints new username
                        break
                    break
                break
            else:
                print ("That username is not added") #prints if user doesn't exist
                userNames.append(userName) #appends username to list
                print ("Your username is "+ userName) #prints new username
                break
        while True:
                password = input("Enter your new eight-digit password ") #asks user for password
                if len(password)<8 or len(password)>8: #makes sure password is exactly 8 digits
                    print("password must be exactly 8 digits ") #tells user that password must be 8 digits
                    continue
                else:
                    passwordCheck = input("Reenter your password ") #asks user to reenter password
                    if passwordCheck == password: #checks if reentered password is equal to initial password
                        passwords.append(password) #adds password to the list 
                        print("Your username and password are now in our system" )
                        break
                    else:
                        continue
                    break
                continue
    if existing == ("No") or existing == ("no"): #if input is no
        while c>0:
            if c>1:
                print (c, " tries remaining ") #prints tries remaining
            if c==1: 
                print (c, " try remaining") #prints tries remaining with correct grammar for 1 try
            userName = input("Enter your Username ") #asks for username
            password = input("Enter your Password ") #asks for password
            if userName in userNames:
                x = userNames.index(userName) #gives the index of the username so that the password can match
                if userNames [userNames.index(userName)] == userName and passwords[userNames.index(userName)] == password: #makes sure that password belong to the username
                    print ("Welcome User! ") #shows succesful login
                    c= 0 #sets the counter to zero to escape the loop
                else:
                    print ("Wrong Username or Password ") #tells the user that username or password is incorrect
                    c = c-1 #lowers the counter
            else:
                print ("Wrong Username or Password ")#tells the user that username or password is incorrect
                c = c-1 #lowers the counter
    c = 3 #resets the loops so a new user has 3 tries left



            
            
    
        
            