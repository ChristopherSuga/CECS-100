# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 09:50:23 2018

@author: chris
"""

grade = eval(input("Enter Grade 1-100 "))
if ((grade>100) or (grade<0)):
    print("error")
if(grade>=90 and grade<=100):
    print("your grade is an A")
if(grade>=80 and grade<=90):
    print("your grade is a B")
if(grade>=70 and grade<=80):
    print("your grade is a C")
if(grade>=60 and grade<=70):
    print("your grade is a D")
if(grade<60):
    print("your grade is an F")
