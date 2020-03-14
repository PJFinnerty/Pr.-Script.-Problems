# This program will calculate a persons BMI using figures provided by the user
# BMI result is the calculation of weight divided by height in meters squared

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in metres squared: "))

#weight = 62
#height = 1.76

#Calculating height in Metres Squared

hm2 = height * height

#Rounding BMI to 2 decimal places

BMI = round (weight / hm2, 2)

print ("Your BMI is", BMI)

