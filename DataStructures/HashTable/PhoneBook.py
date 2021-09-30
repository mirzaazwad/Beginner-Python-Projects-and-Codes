def hashkey(name):
	n=len(name)
	ascSum=0
	for i in range(n):
		ascSum=ascSum+int(ord(name[i]))
	return int(ascSum%n)
hashTable={}
def Insert(name,Number,phoneBook=None):
        if phoneBook==None:
                phoneBook=[None for count in range(hashkey(name)+1)]
                for c in range(hashkey(name)+1):
                        if c==hashkey(name) :
                                Number=str(Number)
                                phoneBook[c]=name+" "+Number
                                print("Number Inserted Successfully")
                                return phoneBook
                        else:
                                phoneBook[c]=None   
        i=hashkey(name)
        if (i+1-len(phoneBook))>0:
                for count in range(len(phoneBook)-1,i):
                        if count==i-1:
                                Number=str(Number)
                                phoneBook.append(name+" "+Number)
                                print("Number Inserted Successfully")
                                return phoneBook
        else:
                for count in range(i+1):
                        if count==i and phoneBook[count]==None:
                                Number=str(Number)
                                phoneBook[count]=name+" "+Number
                                print("Number Inserted Successfully")
                                return phoneBook
                Number=str(Number)
                phoneBook.append(name+" "+Number)
                print("Number Inserted Successfully")
                return phoneBook
def find(name,phoneBook=None):
        if phoneBook!=None:
                i=hashkey(name)
                Found=False
                for c in range(i,len(phoneBook)):
                        cname=phoneBook[c]
                        if phoneBook[c]!=None:
                                if cname[:len(name)]==name:
                                        print(name+"'s Number:"+cname[len(name)+1:])
                                        Found=True
                                        break
                if Found==False:
                        print(name+"'s Number not found")
        else:
                print("Phone Book is empty")
def delete(name,phoneBook=None):
        if phoneBook!=None:
                i=hashkey(name)
                Found=False
                for c in range(i,len(phoneBook)):
                        cname=phoneBook[c]
                        if phoneBook[c]!=None:
                                if cname[:len(name)]==name:
                                        phoneBook[c]=None
                                        print(name+"'s Number "+"deleted successfully")
                                        Found=True
                                        break
                if Found==False:
                        print(name+"'s Number not found")
                return phoneBook
        else:
                print("Phone Book is empty")
                return phoneBook
def inputChoice():
        Error=False
        try:
                choice=int(input("Enter Options: 1 = insert first name and number, 2 = find number, 3 = delete number and 0 = exit from application: "))
                while int(choice)<0 and int(choice)>3:
                        choice=int(input("Invalid Input: Enter Options: 1 = insert first name and number, 2 = find number, 3 = delete number and 0 = exit from application: "))
        except ValueError:
                print("Please enter an integer!")
                Error=True
        if Error==True:
                return inputChoice()
        elif Error==False:
                return choice
def inputString():
        scan=str(input("Enter first name and number as 'someone XXXXXXXX' :"))
        while len(scan)<=11:
                scan=str(input("Error: *Re-Enter first name and number as 'someone XXXXXXXX' :"))
        Error=False
        try:
                for i in range(len(scan)):
                        if scan[i]==chr(32):
                                number=scan[i+1:]
                                number=int(number)                      
        except ValueError:
                print("Error: (1)Check whether you only inserted your first name (2)Check whether you entered a proper 11 digit number with no hyphens")
                Error=True
        if Error==True:
                return inputString()
        elif Error==False:
                return scan
                
                                
                
        
                
                
if __name__ == "__main__":
        count=0
        while True:
                choice=inputChoice()
                if choice==1:
                        scan=inputString()                   
                        for i in range(len(scan)):
                                if scan[i]==chr(32) and count==0:
                                        name=scan[:i]
                                        number=scan[i+1:]
                                        phoneBook=Insert(name,number)
                                        count+=1
                                elif scan[i]==chr(32) and count>0:
                                        name=scan[:i]
                                        number=scan[i+1:]
                                        phoneBook=Insert(name,number,phoneBook)
                elif choice==2:
                        scan=str(input("Enter first name to be found in Phonebook: "))
                        find(scan,phoneBook)
                elif choice==3:
                        scan=str(input("Enter first name to be deleted from Phonebook: "))
                        phoneBook=delete(scan,phoneBook)
                        if phoneBook==None:
                                print("Phone Book is empty, enter option:1 for entry into Phone Book")
                elif choice==0:
                        print("The Phone Book contents are as follows: ")
                        if phoneBook!=None:
                                print("{0:<10}|{1:>10}".format("first name","number"))
                                for i in range(len(phoneBook)):
                                        scan=phoneBook[i]
                                        if scan!=None:
                                                for j in range(len(phoneBook[i])):
                                                        if scan[j]==chr(32):
                                                                name=scan[:j]
                                                                number=scan[j+1:]
                                                                print("{0:<10}|{1:>10}".format(name,number))
                        else:
                                print("Phone Book is empty")
                        break
a=input("Enter to Close program")
                                        
                                                        
                        
                
                        
                        
                                        
                        
                
        
        
                        
        
                        
                
        
        
        
                
                
                

                                
                                

                
        
                                       

        
        
        
                        
                        
                
                
        

            
            
            
            
