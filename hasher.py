#!/usr/bin/python3
import sys
import hashlib
    
def print_banner():
    print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print ("       Simple Sha 256 Hash by ANTO !      ")
    print ("__________________________________________")
    print ("******************************************")
    print ("")
    print (" syntax  ./hasher.py filename.txt")
    return

def makesum(filename):
    print (filename)

def hashit(filename):
    try :
        f =  open(filename,'rb')
        chunk = f.read()
        f.close()
        x= hashlib.sha256(chunk).hexdigest() 
        print("")
        print("")
        print("Sha 256 hash for the file {0} is : {1} ".format(filename,x))
    except IOError as e:
        print (e)
    
    
    
# Checking if argument was provided
if len(sys.argv) <=1:
    print_banner()
    print ("Error ! No filename specified ")
else:
    print_banner()
    hashit(sys.argv[1])
         


     

