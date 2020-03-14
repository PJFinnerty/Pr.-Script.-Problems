#Write a program that takes a positive 
# floating-point number as input and outputs 
# an approximation of its square root. 
# You should create a function called sqrt 
# that does this.
#
# import math
#p = (input("Enter a positive floating point number: "))

#The following example of how to approximate a square root
#found at https://www.youtube.com/watch?v=tUFzOLDuvaE  :

def approxSqrt(num, error = 0.00001):
    guess = num
    diff = 999999999
    while diff > error:
        newGuess = guess - ((guess**2 - num) / (2*guess))

        diff = newGuess - guess
        if diff < 0:
            diff *= -1

        guess = newGuess

    return guess

print(approxSqrt(9))

#Change this formula to display knowledge of how it works:

