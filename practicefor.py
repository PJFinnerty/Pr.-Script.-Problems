#sum = 0
#for i in range(6):
 #   sum = sum + i
  #  print(sum)


#now = datetime.datetime.now(  )
import datetime
now = datetime.datetime.now(  )
day = now.isoweekday( )


w = {'Monday' :1, 'Tuesday':2, 'Wednesday':3, 
'Thursday':4,'Friday':5,'Saturday':6, 'Sunday':7}


for key, value in w.items():
    w = day
    if value <= 5:
        print("No! It's a weekday.")
    else:
        print("It's the weekend!")