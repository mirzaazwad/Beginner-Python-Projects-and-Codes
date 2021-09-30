def binsearch(num,arr):
	Found=False
	midCount=0
	mid=int((len(arr))/2)
	if arr[mid]==num:
		Found=True
		return Found
	elif arr[mid]>num:
		if mid==1:
			if arr[0]==num:#if mid is 1, arr[1]>num then go
#for arr[0] since it is a sorted list and arr[0] is likely to be smaller
				Found=True
				return Found
			else:
				return Found	
		arr=arr[:mid]
		return binsearch(num,arr)
	elif arr[mid]<num:
		if mid==1:
			if arr[2]==num: #if mid is 1, arr[1]<num go
#for arr[2] since it is a sorted list and arr[2] is likely bigger
				Found=True
				return Found
			else:
				return Found
		arr=arr[mid:]
		return binsearch(num,arr)
	else:
		return Found

arr=[1,2,3,6,18,20,22,30,90,78,80]
arr.sort()
num=int(input("Enter a Number: "))
Found=binsearch(num,arr)
if Found==True:
    print("The Number is FOUND in the list")
else:
    print("The Number is NOT FOUND in the list")
