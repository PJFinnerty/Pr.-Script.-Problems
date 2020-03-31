#Peter Finnerty - Week 3 Task

#Create a Program that asks to a user to input a string and then prints to 
# the screen the same string, displaying every second letter in reverse order.
#---------------------------------------------------------------------------------

#Step 1: Create an input prompt with a string asking the user to input a sentence
sentence = (input("Enter a sentence:"))

#Step 2: Using square brackets and two semi-colons to rearrrange the string to print 
#every second character in reverse order.
# Print the output to the screen
print ("Your sentence with every second letter and in reverse order: ", sentence[::-2] )

#Complete