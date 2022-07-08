import datetime
import time
date=datetime.datetime.today()
day= date.strftime("%a")
weekdays=['Mon', "Tue", "Wed","Thur", "Fri"]
for a in weekdays:
    if a == day:
        print ("Date: " , date)
        print ("day: " , day)
        print ("Fare: 100" )
if day == "Sat":
    print ("Date: " , date)
    print ("day: " , day)
    print ("Fare: 60" )
elif day == "Sun":
    print ("Date: " , date)
    print ("day: " , day)
    print ("Fare: 80" )
