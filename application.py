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
    string = string.replace(".","#")
    string = string.replace(",","^")
    string = string.replace("a",",.....|") #there are 6 dots in this line 
    string = string.replace("b",".,....|")
    string = string.replace("c","..,...|")
    string = string.replace("d","...,..|")
    string = string.replace("e","....,.|")
    string = string.replace("f",".....,|")
    string = string.replace("g",",,....|")
    string = string.replace("h",",.,...|")
    string = string.replace("i",",..,..|")
    string = string.replace("j",",...,.|")
    string = string.replace("k",",....,|")
    string = string.replace("l",",,,...|")
    string = string.replace("m",",,.,..|")
    string = string.replace("n",",,..,.|")
    string = string.replace("o",",,...,|")
    string = string.replace("p",",,,,..|")
    string = string.replace("q",",,,.,.|")
    string = string.replace("r",",,,..,|")
    string = string.replace("s",",,,,,.|")
    string = string.replace("t",",,,,.,|")
    string = string.replace("u",",,,,,,|")
    string = string.replace("v","....,,|")
    string = string.replace("w","...,.,|")
    string = string.replace("x","..,..,|")
    string = string.replace("y",".,...,|")
    string = string.replace("z","...,,,|")
    string = string.replace(" ","_")
    string = string.replace("A",",*****|") 
    string = string.replace("B","*,****|")
    string = string.replace("C","**,***|")
    string = string.replace("D","***,**|")
    string = string.replace("E","****,*|")
    string = string.replace("F","*****,|")
    string = string.replace("G",",,****|")
    string = string.replace("H",",*,***|")
    string = string.replace("I",",**,**|")
    string = string.replace("J",",***,*|")
    string = string.replace("K",",****,|")
    string = string.replace("L",",,,***|")
    string = string.replace("M",",,*,**|")
    string = string.replace("N",",,**,*|")
    string = string.replace("O",",,***,|")
    string = string.replace("P",",,,,**|")
    string = string.replace("Q",",,,*,*|")
    string = string.replace("R",",,,**,|")
    string = string.replace("S",",,,,,*|")
    string = string.replace("T",",,,,*,|")
    string = string.replace("U",",,,,,,|")
    string = string.replace("V","****,,|")
    string = string.replace("W","***,*,|")
    string = string.replace("X","**,**,|")
    string = string.replace("Y","*,***,|")
    string = string.replace("Z","***,,,|")
    return string

def decrypt(string):
    string = string.replace("#",".")
    string = string.replace("^",",")
    string = string.replace(",.....|","a") #there are 6 dots in this line 
    string = string.replace(".,....|","b")
    string = string.replace("..,...|","c")
    string = string.replace("...,..|","d")
    string = string.replace("....,.|","e")
    string = string.replace(".....,|","f")
    string = string.replace(",,....|","g")
    string = string.replace(",.,...|","h")
    string = string.replace(",..,..|","i")
    string = string.replace(",...,.|","j")
    string = string.replace(",....,|","k")
    string = string.replace(",,,...|","l")
    string = string.replace(",,.,..|","m")
    string = string.replace(",,..,.|","n")
    string = string.replace(",,...,|","o")
    string = string.replace(",,,,..|","p")
    string = string.replace(",,,.,.|","q")
    string = string.replace(",,,..,|","r")
    string = string.replace(",,,,,.|","s")
    string = string.replace(",,,,.,|","t")
    string = string.replace(",,,,,,|","u")
    string = string.replace("....,,|","v")
    string = string.replace("...,.,|","w")
    string = string.replace("..,..,|","x")
    string = string.replace(".,...,|","y")
    string = string.replace("...,,,|","z")
    string = string.replace(",*****|","A") 
    string = string.replace("*,****|","B")
    string = string.replace("**,***|","C")
    string = string.replace("***,**|","D")
    string = string.replace("****,*|","E")
    string = string.replace("*****,|","F")
    string = string.replace(",,****|","G")
    string = string.replace(",*,***|","H")
    string = string.replace(",**,**|","I")
    string = string.replace(",***,*|","J")
    string = string.replace(",****,|","K")
    string = string.replace(",,,***|","L")
    string = string.replace(",,*,**|","M")
    string = string.replace(",,**,*|","N")
    string = string.replace(",,***,|","O")
    string = string.replace(",,,,**|","P")
    string = string.replace(",,,*,*|","Q")
    string = string.replace(",,,**,|","R")
    string = string.replace(",,,,,*|","S")
    string = string.replace(",,,,*,|","T")
    string = string.replace(",,,,,,|","U")
    string = string.replace("****,,|","V")
    string = string.replace("***,*,|","W")
    string = string.replace("**,**,|","X")
    string = string.replace("*,***,|","Y")
    string = string.replace("***,,,|","Z")
    string = string.replace("_"," ")
    return string
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

    #if hold == ("devdelete"):
    #   devdelete()
    

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
        askpass = input("what would you like your new password to be? ")
        encode = encrypt(askpass)
        f.write(encode)
    if hold == ("1"):  
        print ("deleting password file.")
        os.remove("password.txt")
        return
def askpassword():
    f = open("password.txt","r")
    readfile = f.read()
    pastpass = decrypt(readfile)
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
    hold2 = input ("Whats on your mind? >>> ")
    f = open(f"{currentday2}.txt","w")
    hold3 = encrypt(hold2)
    f.write (f"{hold3} - {currentday1.strftime('%I:%M:%S %p')}")
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
        rawtext = (f.read())
        hold = decrypt(rawtext)
        print (hold)
        bomb = bomb+1
        return
    if reading not in lucky:
        try:
            readingint = int(reading)
            holdtextfile = (textfile[readingint-1])
            f = open(holdtextfile, "r")
            rawtext = (f.read())
            hold = decrypt(rawtext)
            print (hold)
            startpro()
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
