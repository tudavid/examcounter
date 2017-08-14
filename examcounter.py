from datetime import datetime, timedelta
import os

exams = open((os.path.dirname(__file__) + "/examdates"), "r")
listofexamdates = []
datecounter = 0
while (datecounter < 6):
    for line in exams:
	    parts = line.split(";")
	    counter = 0
	    for i in parts:
		    #print i
		    if(counter % 2 == 1):
			    examdate = datetime.strptime(i, '%Y-%m-%d %H:%M:%S ')
			    currentdate = datetime.now()
			    timebetween = examdate - currentdate
			    if(timebetween >=  timedelta(minutes=0)):
			        pair1 = timebetween
			        pair = pair2, pair1
			        listofexamdates.append(pair)
		    else:
			    pair2 = i
		    counter+=1
    datecounter+=1
listofexamdates.sort(key=lambda x: x[1])
output=" "
for j in listofexamdates:
	a,b = j
	output +=a + ":" + " " + "["
	output += str(b.days) + "d"
	output += str(b.seconds//3600) + "h"
	#output += str((td.seconds//60)%60) + "m"
	output += "] "
print output
