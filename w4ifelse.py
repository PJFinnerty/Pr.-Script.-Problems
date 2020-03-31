#Peter Finnerty - Week 4 Task

#Write a program that asks the user to input any positive integer 
# and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, 7
# if it is even, divide it by two, but if it is odd, 
# multiply it by three and add one. 
# Have the program end if the current value is one.
#------------------------------------------------------------------------------------
#Create a variable called 'q' and use an input prompt
#asking the user to enter a positive integer.
q = int(input("Input a positive integer: "))

#Create a variable called 's' and assign it the value of 2.
s = 2

#By calculating the modulus of 'q'/'s', determine if the input 
# is even or odd.
while (q != 1):
     #Use an 'if' statement to take an even input
        #and divide it by 2.
    if q % s == 0:
        print(q/2)
        break
     #The else statement will take an even input and
     #multiply by 3, then add 1.
    else:
        print(q * 3 + 1)
        break

#Complete.