array=[6,5,3,1,8,7,2,4]
for i in range(len(array)):
    temp = array[i]
    
    count = i-1
    while count >= 0:
        if array[count] > temp:
            array[count+1] = array[count]
        else:
            break
        
        count-=1
    array[count+1] = temp
    
print(array)
        
            

            
            
        
        
