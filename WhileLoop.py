# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 08:26:37 2018

@author: chris
"""

count = 0
while True:
    number = int(input("enter a number between 10 and 20 ")) 
    if number >=10 and number <=20:
        break
    else:
        count = count + 1
        print("this number is invalid")
        print("you have entered ", count, "invalid numbers")
        print("enter a new number")
print("you entered " ,number)
print("this answer is valid")
print("invalid numbers entered: ", count)