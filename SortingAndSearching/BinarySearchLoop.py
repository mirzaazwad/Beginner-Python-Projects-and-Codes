arr=[1,2,3,6,18,20,22,30,90,78,80]
searchitem=int(input("Enter Item to be searched: "))
found=False
searchfailed=False
first=0
last=len(arr)-1
while not found and not searchfailed:
    middle=(first+last)//2
    if arr[middle]==searchitem:
        found=True
    else:
        if first>=last:
            searchfailed=True
        else:
            if arr[middle]>searchitem:
                last=middle-1
            else:
                first=middle+1
if found==True:
    print("The position where value is found is: {0} \n and value is: {1}".format(middle,arr[middle]))
else:
    print("Item not present in array")
    
