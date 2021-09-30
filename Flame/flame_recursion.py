StringInput=str(input("Please Enter a Sentence to be Flamed:"))
charList=list(StringInput)
for i in range(len(charList)):
    if charList[i]==chr(32):
        charList[i]=None
print(charList)
array=[None for i in range(len(charList))]
maxarr=[1,0,0]
while True:
    if len(array)==2 or array==maxarr:
        break
    else:
        if len(array)==len(charList):
            array=[]
            for i in range(len(StringInput)):
                charVar=charList[i]
                n=1
                for j in range(i+1,len(StringInput)):
                        if charVar==None: #Overlooks newly intialised None values
                            break
                        elif charVar==charList[j]:
                            n+=1
                            charList[i]=None
                            charList[j]=None
                if (charVar!=None):
                    array.append(n)
        count=0
        print(array)
        reversecount=len(array)
        if reversecount%2==0:
            temparray=[]
            while count!=reversecount:
                reversecount-=1 #decremented at start which helps keep the value of count-reverse count as a constant 0
                numberTemp=array[count]+array[reversecount]
                if numberTemp>9:
                    Temp=numberTemp-10
                    temparray.append(1)
                    temparray.append(Temp)
                else:
                    temparray.append(numberTemp)
                count+=1#incremented at end so that the index value 0 is processed and count increases to 1 as reversecount decreases by n=n-- so that eventually reversecount-count becomes 0, where n is an odd number
            array=temparray
        else:
            reversecount-=1
            limit=(len(array)/2)
            temparray=[]
            for i in range(int(limit)+1):
                if i!=reversecount:
                    numberTemp=array[i]+array[reversecount]
                    if numberTemp>9:
                        Temp=numberTemp-10
                        temparray.append(1)
                        temparray.append(Temp)
                    else:
                        temparray.append(numberTemp)
                    reversecount-=1
                else:
                    temparray.append(array[i])
            array=temparray
numList=array
print(array)
print(charList)
if numList==[1,0,0]:
    Result=100
else:
    Result=numList[0]*10+numList[1]
print("The Result of the number being flamed is:",Result,sep=' ')
input("Press Enter to Continue")

            
            
                
            

        
    
