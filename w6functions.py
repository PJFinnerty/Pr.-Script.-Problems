# Peter Finnerty - Weekly Task 6

# Write a program that takes a positive floating-point number as input 
# and outputs an approximation of its square root. 
# You should create a function called sqrt that does this.

#   λ w6functions.py
#   Enter the positive float which you require the square root of: 355
#   Enter 1 guess for the square root: 22
#   Minimum guess limit permitted is 7. Enter a maximum guess count (>7) : 10
#   18.8414
#-------------------------------------------------------------------------------
 
# Create prompts for user to input no. to be squared, a guess at what the root is
# and a guesslimit that must be over 7. 
rooted = float(input("Enter the positive float which you require the square root of: ") )
guess = float(input("Enter 1 guess for the square root: "))
guesslim = float(input("Minimum guess limit permitted is 7. Enter a maximum guess count (>7) : "))

# Use 'if' loop to ensure guess limit is > 7. 
# This will ensure that the ensure that user input a guess count 
# high enough to ensure an accurate approximation.
if guesslim <= 7:
    print("Guess count must be greater than 7.")
else:
    #Create function 'sqrt' utilsing variables.
    def sqrt(rooted, guess, guesslim):
        squareroot = guess
        # Set guess limit to decrease by 1 with each increment.
        guesslim = guesslim - 1
        # Assign new guesslim of greater than 0.
        while guesslim > 0:
            # Use 'Babylonian Method', decreasing 'guesslim'
            # by 1 with each iteration.
            squareroot =  (squareroot + (rooted / squareroot)) / 2
            guesslim = guesslim - 1
        #Return the squareroot of 'rooted' rounding to 4 decimal points.    
        return round(squareroot, 4)
    print( sqrt(rooted, guess, guesslim) )

    # Complete.

# Line 17-18; Line 29: Information on calculating square root using Babylonian method found @ 
# https://blogs.sas.com/content/iml/2016/05/16/babylonian-square-roots.html

#Line 21; Line 24; Line 26 and line 30: Information on using decreasing 'guesslim' by 1 for 
# each increment found at @
# https://github.com/ianmcloughlin/pyprimes/blob/master/functions.py