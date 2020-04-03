# Peter Finnerty - Week 3 Task

# Create a Program that asks to a user to input a string and then prints to 
# the screen the same string, displaying every second letter in reverse order.
#---------------------------------------------------------------------------------

# Create an input prompt with a string asking the user to input a sentence
sentence = (input("Enter a sentence:"))

# Create an indexing operator using square brackets. Leave the first two index fields empty.
# In the third index field, enter -2. The minus sign will run the string in reverse 
# (starting from the final character) up to the first, the index number (2) skips
# every second letter of the string. Enclose the operator in a print function.
print ("Your sentence with every second letter and in reverse order: ", sentence[::-2] )

#Complete.