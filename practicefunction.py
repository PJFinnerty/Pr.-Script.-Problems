#Peter Finnerty

#Practice file for Week 6 functions task.

#The following method for calculating a square root uses the repetitious
# method, where each new guess of the square root, is the previous result
# of the following calculation: (guess + (rooted number / guess) ) /2

#This is a repetitious method and is similar to how Banylonian Square root
#method works.
#-----------------------------------------------------------------------------------

rooted = float(input("Enter number which you require a square root to be found: ") )
guess1 = float(input("Enter user guess for the square root: "))
print("User has guessed that the square root of", rooted, "is", guess1,"\n")

new = (guess1 + (rooted / guess1 ) ) / 2 
#---------------------------------
guess2 = new
new2 = (guess2 + (rooted / guess2 ) ) /2 
#---------------------------------
guess3 = new2
new3 = (guess3 + (rooted / guess3 ) ) / 2
#---------------------------------
guess4 = new3
new4 = (guess4 + (rooted / guess4) ) / 2
#---------------------------------
guess5 = new4
new5 = (guess5 + (rooted / guess5) ) / 2
#---------------------------------
guess6 = new5
new6 = (guess6 + (rooted / guess6) ) / 2
#---------------------------------
guess7 = new6
new7 = (guess7 + (rooted / guess7) ) / 2

final = round (new7, 4)
print("The 'approximate' square root of", rooted, "is actually", final)