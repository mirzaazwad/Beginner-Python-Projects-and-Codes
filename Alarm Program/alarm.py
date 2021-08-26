import time
from subprocess import call
print("Alarm v1.0")
tstr=str(input("Enter Time for Alarm to Ring as hours:minAM/PM or hours:minam/pm : "))
while True:
	try:
		if len(tstr)>7 or len(tstr)<6:
			tstr=str(input("Error Entry of Time, Please re-enter with correct format hours:minAM/PM (too long or too short) : "))
		else:
			if (tstr[1]==":" or tstr[2]==":"):
				timearr=[int(tstr[:-5]),int(tstr[-4:-2]),tstr[-2:].upper()]
				if timearr[0]<=12 and timearr[0]>=1:
					if timearr[1]<=60 and timearr[1]>=0:
						if timearr[2] in ("AM","PM"):
							timearr=[int(tstr[:-5]),int(tstr[-4:-2]),tstr[-2:].upper()]
							break
						else:
							tstr=str(input("Error Entry of Time, Please re-enter with correct format hours:minAM/PM (Enter AM or PM: "))
					else:
						tstr=str(input("Error Entry of Time, Please re-enter with correct format hours:minAM/PM (Minutes are between 0 and 60) : "))
				else:
					tstr=str(input("Error Entry of Time, Please re-enter with correct format hours:minAM/PM (Hours are between 1 and 12) : "))
			else:
				tstr=str(input("Error Entry of Time, Please re-enter with correct format hours:minAM/PM , example- 9:32PM :"))
	except ValueError:
		tstr=str(input("Error Entry of Time, Please re-enter with correct format hours:minAM/PM, please enter numbers for hours and minutes : "))
		continue
def secs(arr):
	if (arr[0]==12 and arr[2]=="AM"):
		secs=0+arr[1]*60
	elif (arr[0]==12 and arr[2]=="PM"):
		secs=arr[0]*3600+arr[1]*60
	elif arr[2]=="PM":
		secs=arr[0]*3600+arr[1]*60+12*3600
	elif arr[2]=="AM":
		secs=arr[0]*3600+arr[1]*60
	return secs
while True:
	target=secs(timearr)
	cur_time=time.time()+6*60*60
	currenttime=cur_time % (24*60*60)
	if currenttime>=target:
		print(" \n \n \n \n \n \n Ringing Alarm \n \n \n Time =  |{0:<10}:{1:^10} {2:>10}| \n \n \n \n \n \n".format(timearr[0],timearr[1],timearr[2]))
		call("ffplay Alarm2.mp4",shell=True)
		break

		

		

