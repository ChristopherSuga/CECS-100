# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 09:46:09 2017

@author: gg363d
"""

# This function is responsible to check the user input for the meteric.
# The function will only reurn True if the input is correct and Fals if its not.
def checkInput(metric):
    metricList = ["Pounds", "Grams" , "Kilograms", "Meter", "Centimeter", "Feet", "Inches" ]
    if metric in metricList:
        return True
    else:
        print("That is not a correct Metric System. ")
        return False
# This function expects two inputs (height and meteric)  and it will only return
# the hieght in the correct meteric
def checkHeight(height, metric):
    if metric == ("Meters"):
        height = height * 39.37
    if metric == ("Centimeters"):
        height = height / 2.54
    if metric == ("Feet"):
        height = height * 12
    if metric == ("Inches"):
        height = height * 1
    return height
# This function expects two inputs (weight and meteric)  and it will only return
# the weight in the correct meteric.   
def checkWeight(weight, metric):
    if metric == ("Pounds"):
        weight = weight * 1
    if metric == ("Grams" ):
        weight = weight / 453.592
    if metric == ("Kilograms"):
        weight = weight * 2.205
    return weight
# This function takes the "bmi" as an input and it will provide advice to the user based on the "bmi" result.
def checkBMIresult(bmi):
    if bmi<=0:
        print("Error")
    if bmi >25:
        print("Eat less food")
    if bmi >20 and bmi <=25:
        print("Eat the same amount of food")
    if bmi <19 and bmi>0:
        print("Eat more food")
        
# The main function will capture the user input and it will call the above functions accodingly       
def main ():
    ifTrue = True
    while ifTrue == True:
        heightInput = eval(input("Enter your height "))
        heightMetric = input("Meters, Centimeters, Feet, or Inches? ")
        ifTrue = checkInput(heightMetric)
        print(ifTrue)
        weightInput = eval(input("Enter your weight "))
        weightMetric = input("Pounds, Grams, or Kilograms? ")
        ifTrue = checkInput(weightMetric)
        print(ifTrue)
        height = checkHeight(heightInput, heightMetric)
        weight = checkWeight(weightInput, weightMetric)
        if heightMetric == ("Inches"):
            print("You are " + str(heightInput) + " " + str(heightMetric) +" tall ")
        else:
            print("You are " + str(heightInput) + " " + str(heightMetric) +" tall or " + str(height) +" Inches tall " )
        if weightMetric ==("Pounds"):
            print("You weigh " + str(weightInput) + " " + str(weightMetric))
        else:
            print("You weigh " + str(weightInput) + " " + str(weightMetric) +" or " + str(weight) + " Pounds ")
        bmi = (weight / height**2)* 703
        print("Your BMI is " + str(bmi))
        checkBMIresult(bmi)
        
main()