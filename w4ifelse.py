# Peter Finnerty - Week 4 Task

# Write a program that asks the user to input any positive integer and outputs 
# the successive values of the following calculation. At each step calculate the 
# next value by taking the current value and, 7 if it is even, divide it by two,
# but if it is odd, multiply it by three and add one. 
# Have the program end if the current value is one.
#------------------------------------------------------------------------------------

# Create a variable called 'q' and use an input prompt to ask the user 
# to enter a positive integer.
q = int(input("Input a positive integer: "))
s = 2
print(q, end = " ")

# Set the while loop to finish iterations when q = 1.
while q > 1:
    # By calculating the modulus of 'q'/'s', determine if the input is even or odd.
    # Create an 'if' statement to take an even input and divide it by 2 ('s').
    if q % s == 0:
        q = q/2
        q = int(round(q) )
        print(q, end = " ")

    # Create an 'else' statement to take an odd input and multiply it by 3, then add 1.
    else:
        q = (q * 3) + 1
    # In both 'if' and 'else' loops, round output to remove 0, and remove end line characters.
    # This ensures that the returned figurs appear across the line(s) and are more readable.
        q = int(round(q) )
        print(q, end = " ")

# Complete

# Lines 14 and 19: Information on EOF character found @
# https://stackoverflow.com/questions/3249524/print-in-one-line-dynamically