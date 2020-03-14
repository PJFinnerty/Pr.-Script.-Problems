#Write a program that asks the user to input any 
# positive integer
#and outputs the successive values of the 
# following calculation.
# At each step calculate the next value by 
# taking the current value and, if it is even,
# divide it by two, but if it is odd, 
# multiply it by three and add one. 
# Have the program end if the current 
# value is one.

q = int(input("Input a positive integer: "))
s = 2

while (q != 1):
    if q % s == 0:
        print(q/2)
        break
    else:
        print(q * 3 + 1)
        break







