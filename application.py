import datetime
import os
import random
from time import sleep
help = ["Help", "help", "?"]
secondstp = ["create", "Create", "append", "Append", "write","Write"]
view = ["history","History","View","view"]
lucky = ["Im feeling lucky", "I'm feeling lucky","IFL","Lucky","random","Random","i'm feeling lucky","im feeling lucky"]
delete = ["delete","Delete","trash","Trash"]
sure = ["Y","y","Yes","yes"]
nope = ["N","n","no","No"]
passlist = ["pass","Pass","Password","password"]
currentday1 = datetime.datetime.now()
currentday2 = currentday1.strftime("%m %d %Y %A")
extension = ".txt"
print (currentday2),

def encrypt(string):

    return

def unecnrypt(string):

    return
def startpro():
    print ("What do you want to do?")
    print ("Type 'help' for assistance")
    hold = input(">>>")
    
    if hold in help:
        needhelp()
    if hold in secondstp:
        try:
            f = open(f"{currentday2}.txt","x")
            midway() 
        except:
            print ("")
            return
    if hold in view:
        askpassword()
        return 
    if hold in delete:
        deletefun()
        return 
    if hold in passlist:
        print ("""which would you like to do
               1. Create a new password
               2. Edit a new password""")
        oneortwo = ["1","2"]
        gotowhat = input(">>>")
        if gotowhat == ("1"):
            createpassword()
        if gotowhat == ("2"):
            createnewpassword()

    if hold == ("devdelete"):
       devdelete()

def devdelete():
     print ("Deleting password")
     os.remove("password.txt")
     startpro()

def createpassword():
     try: #if the file does not exist
            f = open("password.txt", "x")
            f.close
            print("password file created. Returning to the start of the program.")
            startpro()
            return
     except: #if it does exist 
        print ("You already have a password saved. Please edit your old one")
        f.close
        startpro()

def createnewpassword():
    f = open("password.txt","w")
    print ("""Which would you like to do
                    1. delete old password
                    2. create new password""")
    hold = input(">>>")
    if hold == ("2"):
        askpass = input("what would you like your new password to be?")
        f.write(askpass)
    if hold == ("1"):  
        print ("deleting password file.")
        os.remove("password.txt")
        return
def askpassword():
    f = open("password.txt","r")
    pastpass = f.read()
    hold = input ("Please input your password ")
    if pastpass == hold:
        f.close
        history()
    if pastpass != hold:
        f.close
        print ("wrong password. Sending you to the start of the program.")
    return
        
def needhelp():
    print ("""
> Help -- displays this menu
> Create -- creates a new entry
> View -- View previous entries:
           Random -- Get a random entry
           Integer -- get entry from displayed list
> Delete -- Delete saved entries
> Password -- create and manage password  
> Settings -- Unfinished         

           
           """)
    startpro()

def midway():
    hold2 = input ("Whats on your mind? >>>")
    f = open(f"{currentday2}.txt","w")
    f.write (f"{hold2} - {currentday1.strftime('%I:%M:%S %p')}")
    f.close 
    
def history():
    bomb = 0
    x=0
    files = os.listdir()
    textfile = [file for file in files if os.path.splitext(file)[1] == extension]
    textfilelen = len(textfile)
    imfeelinglucky = random.randint(0, textfilelen)
    
    while x != textfilelen:
        print (f"> ({x+1}) {textfile[x]}")
        x = x+1
        if x == textfilelen:
            break
    
    reading = input("Which entry do you want to read? ")
    if reading in lucky:
        randomtextfile = (textfile[imfeelinglucky])
        f = open(randomtextfile, "r")
        print (f.read())
        bomb = bomb+1
        return
    if reading not in lucky:
        try:
            readingint = int(reading)
            holdtextfile = (textfile[readingint-1])
            f = open(holdtextfile, "r")
            print (f.read())
            return
        except: 
            return
        
def deletefun():
    x=0
    files = os.listdir()
    textfile = [file for file in files if os.path.splitext(file)[1] == extension]
    textfilelen = len(textfile)
    while x != textfilelen:
        print (f"> ({x+1}) {textfile[x]}")
        x = x+1
        if x == textfilelen:
            break
    reading = input("Which entry do you want to delete? ")
    readingint = int(reading)
    areyousure = input("Are you sure Y/N  ")
    if areyousure in sure:
        os.remove (textfile[readingint-1])
        print ("File deleted.")
    if areyousure in nope:
        print ("returning to beginning")
        startpro()


startpro()