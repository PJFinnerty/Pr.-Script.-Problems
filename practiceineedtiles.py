 #This program calculates tiles required
#on walls or floors (in metres squared)

length = float (input ("Enter room length: "))
width = float (input ("Enter room width: "))

area = length * width

needed = area * 1.05 

print ("You need", needed, "tiles in metres squared.")

