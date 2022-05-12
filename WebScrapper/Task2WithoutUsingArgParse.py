#Task2 without using ArgumentParser 
import re
import sys
import os
import urllib.request, urllib.error, urllib.parse

#Step 00: Output Folder from URL
def outputFolderName(url):
    path=os.path.dirname(url)
    protocol=["http:", "https:", "ftp:"]
    if(os.path.basename(path) in protocol):
        return "/"
    return os.path.basename(path)

#Sep 01: URL Validation
def isProtocolValid(url):
    protocol=["http://", "https://", "ftp://"]#length is 7,6 and 8 characters for each string
    if((url[0:6] in protocol) or (url[0:7] in protocol) or (url[0:8] in protocol)):
        return True
    return False

def getProtocol(url):
    protocol=["http://", "https://", "ftp://"]#length is 7,6 and 8 characters for each string
    if(url[0:6] in protocol):
        return protocol[2]
    elif(url[0:7] in protocol):
        return protocol[0]
    elif(url[0:8] in protocol):
        return protocol[1]
    else:
        print("Invalid Protocol")
        sys.exit(-1)
    
def isSubdomainNameValid(url):
    protocol=["http://", "https://", "ftp://"]#length is 7,6 and 8 characters for each string
    validDomains=[".com",".org",".edu",".mil",".net",".gov"]
    protocolEnd=0
    if(url[0:6] in protocol):
        protocolEnd=6
    elif(url[0:7] in protocol):
        protocolEnd=7
    elif(url[0:8] in protocol):
        protocolEnd=8
    else:
        sys.exit(-1)
    domainStart=0
    length=len(url)
    if(length-4<=0):
        return False
    for i in range(length-4):
        if(url[i:i+4] in validDomains):
            domainStart=i
            break
    if(domainStart-protocolEnd>3):
        return True
    elif(domainStart-protocolEnd==3 and url[protocolEnd:domainStart]!="www"):
        return True
    else:
        return False
    
    
def isDomainNameValid(url):
    validDomains=[".com",".org",".edu",".mil",".net",".gov"]
    for i in range(6):
        if(validDomains[i] in url):
            return True
    return False

# class InvalidURLException(Exception):
#     pass

def isValidURL(url):
    if(isDomainNameValid(url) and isProtocolValid(url) and isSubdomainNameValid(url)):
        return True
    else:
        print(url)
        if(not isDomainNameValid(url)):
            print("Domain Name is not valid, make sure it is .com/.org/.net/.gov/.mil/.edu")
        if(not isSubdomainNameValid(url)):
            print("Subdomain name is not valid make sure it is present")
        if(not isProtocolValid(url)):
            print("Protocol is not valid, accepted protocols are http:// https:// and ftp://")
        return False
def isScrappable(url):
    if(isDomainNameValid(url) and isProtocolValid(url) and isSubdomainNameValid(url)):
        return True
    else:
        return False
#Step 02: Download html files and saving it
def downloadedFiles(url):
    response = urllib.request.urlopen(url)
    webContent = response.read().decode('UTF-8')
    return webContent
    
def getFileName(url):
    path=os.path.dirname(url)
    difference=len(url)-len(path)
    return url[len(path):len(path)+difference]  

def determineFileExtension(url):#For images only
    length=len(url)
    i=length-1
    while(i>=0):
        if(url[i]=='.'):
            break
        i-=1
    if(length-i>5):
        return ".jpeg"
    return url[i:]
        
    

if  __name__=='__main__':
    argumentsGiven=len(sys.argv)#step 04: Using command line arguments(begin)
    WorkingDirectory=""
    if(argumentsGiven==1):
        print("No arguments given so program terminated")
        sys.exit(-1)
    elif(argumentsGiven==2):
        print("Default output location set as current working directory")
        WorkingDirectory=os.path.dirname(os.path.realpath(__file__))+"/" #saves as html file
    else:
        WorkingDirectory=str(sys.argv[2])
    url=str(sys.argv[1])#step 04: Using command line arguments(end)
    print("Folder Name: ",outputFolderName(url))
    if(not isValidURL(url)):
        #raise InvalidURLException("The URL you entered is not valid") #intially I thought of raising an exception as a better option
        print("Please enter valid URL")
        sys.exit(-1)
    #Step 2 bonus task: Save to file
    htmlCode=downloadedFiles(url)
    fileHandler=open(WorkingDirectory+"Task2.html","w", encoding="utf-8")#saving html for step 02
    fileHandler.write(htmlCode)
    fileHandler.close()
    imgTags=re.findall("""<img\s.*?src=(?:'|")([^'">]+)(?:'|")""",htmlCode) #Step 03: Using regular expressions, find every image tag (<img>) in
#the website
    length=len(imgTags)
    for i in range(length):
        if(imgTags[i][0:2]=="//"):
            imgTags[i]=getProtocol(url)+imgTags[i][2:]
        if(not isScrappable(imgTags[i])):
            print("This image url probably has a base tag so url invalid cannot be scrapped")
            continue
        print(imgTags[i])#the printing is to check for process
        f = open(WorkingDirectory+str(i)+determineFileExtension(imgTags[i]),'wb')#Step 03: Save images to file or basically download images
        f.write(urllib.request.urlopen(imgTags[i]).read())
        f.close()
    
    
    
    
    
