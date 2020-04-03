# Peter Finnerty - Week 2 Task
 
# Write a program that will calculate a persons BMI using figures provided
# by the user
# BMI result is the calculation of weight divided by height in meters squared
#-----------------------------------------------------------------------------

#Create 2 input prompts for the user
#requesting that the user input their weight and height in m2
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in metres squared: "))

#Calculate height in Metres Squared and assign it the
#variable name hm2
hm2 = height * height

#Create a variable named BMI that divides weight by
# 'hm2' and round it to 2 decimal places
BMI = round (weight / hm2, 2)

#Printing output to screen
print ("Your BMI is", BMI)

#Complete