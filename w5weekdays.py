#Write a program that outputs whether or not 
# today is a weekday. An example of running 

#i will need a boolean to show if its a weekday or not
#i will NOT need an input promt for the user
#i will need to use the datetime class to output
#the result



import datetime
#print(now)
#print(day)

now = datetime.datetime.now(  )
day = now.isoweekday( )

w = {'Monday - Weekday' :1, 'Tuesday - Weekday':2, 'Wednesday - Weekday':3,
 'Thursday - Weekday':4,'Friday - Weekday':5,'Saturday - Weekend!':6, 
 'Sunday - Weekend!':7}

for key, value in w.items():
    if value == now.isoweekday():
      print(key)



#while day == now.isoweekday( ):
   #if day <= 5:
    # print("No! It's a weekday.")
   #else: 
    # print("It's the weekend!")



  
    
    

    

 
   #if value == 2:
    #    print("No! It's a weekday.")
    #if value == 3:
      #  print("No! It's a weekday.")
    #if value == 4:
     #   print("No! It's a weekday."
    #if value == 5:
     #   print("No! It's a weekday." 

#for values in w.values( ):
 #   if w == 'Monday':
  #      print("yay!")



#for key in w.keys():
    #print(keys)

#for values in w.values( ):
     #print(values)











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

