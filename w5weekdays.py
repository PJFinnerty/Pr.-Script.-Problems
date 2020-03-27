#Peter Finnerty - Week 5 Task

#Write a program that outputs whether or not today is a weekday. 
#I will need to use the datetime class to output
#the result.

#Step 1: Import datetime.
import datetime

#Step 2: create a variable called 'now' and assign it 
#the datetime.now method.
now = datetime.datetime.now(  )

#Step 3: Create the variable 'day', and assign it the isoweekday
#method.
day = now.isoweekday( )

#Step 4: Creat a dictionary called 'w' with 7 elements, each entry should
#correspond to the 7 possible returns for the iso.weekday class.
w = {'Today is a weekday.':1, 'Today is a weekday.':2, 'Today is a weekday.':3,
 'Today is a weekday.':4,'Today is a weekday.':5,'It is the weekend, yup!':6, 
 'It is the weekend, yup!':7}

#Step 5: Use a 'for' loop to inspect the value of the iso.weekday return
#to see which of the values in 'w' that it matches - print the 
#corresponding key.
for key, value in w.items():
    if value == now.isoweekday():
      print(key)

#Complete.


#https://stackoverflow.com/questions/19167276/
# pythonic-simplest-way-to-create-range-of-
# weekday-date-objects - ref user 'Marko'
#sdate = datetime.date(2020, 3, 2)
#edate = datetime.date(2020, 3, 8)
#weekdays = [sdate + datetime.timedelta(days=i) 
            #for i in range((edate - sdate).days+1)
            #if (sdate + datetime.timedelta(days=i)
            #).weekday() not in (5, 6)]
            
#print(i)



#result = now.weekday( )
#if result = 0:
#    daycheck = True

#An example of runningthis program on a Thursday is given below.
#$ python weekday.py
#Yes, unfortunately today is a weekday.

#An example of running it on a Saturday
#  is as follows.
#$ python weekday.py
#It is the weekend, yay!

#tday = datetime.date.today(  ) 
#print(tday.isoweekday( ) )

#tday = datetime.timedelta (days = 6)
#print(tday + tdelta)

#bday = datetime.date(2020, 4, 6)

#till_bday = bday - tday

#print(till_bday.total_seconds())

