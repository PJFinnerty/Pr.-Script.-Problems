# Peter Finnerty - Week 5 Task

# Write a program that outputs whether or not today is a weekday.
#-----------------------------------------------------------------------

# Import datetime.
import datetime

# Create a variable called 'now' and assign it the datetime.now function.
now = datetime.datetime.now(  )

# Create the variable 'day', and assign it to the isoweekday function.
day = now.isoweekday( )

# Create a dictionary called 'w' with 7 elements. Each entry should
# correspond to the 7 possible returns from the iso.weekday function.
w = {'Today is a weekday.':1, 'Today is a weekday.':2, 'Today is a weekday.':3,
 'Today is a weekday.':4,'Today is a weekday.':5,'It is the weekend, yup!':6, 
 'It is the weekend, yup!':7}

# Use a 'for' loop to inspect the value of the iso.weekday return to see 
# which of the values in 'w' that it matches - print the 
# corresponding key.
for key, value in w.items():
    if value == now.isoweekday():
      print(key)

#Complete.

#lines 26-28: Information on datetime use found @
#https://stackoverflow.com/questions/19167276/
# pythonic-simplest-way-to-create-range-of-
# weekday-date-objects
