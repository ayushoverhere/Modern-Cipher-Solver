import sys
import re
def display():
    print("Modern Cipher Solver\n")
    print("\nEnter 'C' for Caesar Cipher \nEnter 'M' for Multiplicative Cipher\n ")
    while True:
        cc = (input("Please enter your choice: "))
        if cc not in ('C', 'M'):
            print("Not an appropriate choice!")
        else:
            break
    
    if cc == 'M':
        print("\nMultiplicative Cipher\n")
        print("MENU:\nEnter 'E' for ENCRYPTION \nEnter 'D' for DECRYPTION \nEnter 'B' for BRUTE_FORCE \nEnter 'X' for Exit \n ")
        choice()
    else:
        print("\nCaesar Cipher\n")
        print("MENU:\nEnter 'E' for ENCRYPTION \nEnter 'D' for DECRYPTION \nEnter 'B' for BRUTE_FORCE \nEnter 'X' for Exit \n ")
        choice2()
def choice():

    while True:
        ch = (input("Please enter your choice: "))
        if ch not in ('E', 'D', 'B','X'):
            print("Not an appropriate choice!")
        else:
            break
   
    if(ch == 'E'):
        print("\nWelcome to Encryption\n")
        encryption()
    elif(ch == 'D'):
        print("\nWelcome to Decryption\n")
        decryption()
    elif(ch == 'B'):
        print("\nWelcome to Brute_Force\n")
        brute_force()
    elif(ch == 'X'):
        exit("\nHmm, The program is now terminated! \n")
        
    else:  
        choice()
      
print()

def choice2():
    
    while True:
        ch = (input("Please enter your choice: "))
        if ch not in ('E', 'D', 'B', 'X'):
            print("Not an appropriate choice.")
        else:
            break
    
    if(ch == 'E'):
        print("\nWelcome to Encryption\n")
        encryption2()
    elif(ch =='D'):
        print("\nWelcome to Decryption\n")
        decryption2()
    elif(ch == 'B'):
        print("\nWelcome to Brute_Force\n")
        brute_force2()
    elif(ch == 'X'):
        exit("\nHmm, The program is now terminated! \n")
    else:  
        choice2()
      
print()
def plain_text():
    while True:
        plt = input("Enter plain text: ").strip()
        if plt.isalpha() or bool(re.search(r"\s", plt)):
            return plt.upper()
            break
        else:
            print("Sorry, I didn't understand that.")
def ciper_text():
    while True:
        clt = input("Enter ciper text: ").strip()
        if clt.isalpha() or bool(re.search(r"\s", clt)) :
            return clt.upper()
            break
        else:
            print("Sorry, I didn't understand that.")
def key():
    while True:
        key = input("Enter the key: ")
        if key.isdecimal():
            return key
            break
        else:
            print("Invalid key entered!") 
            
def encryption2():
    ct = ""
    pt = plain_text()
    k = int(key())
    try:
    
        k = k % 26
        sum = 0
        for i in pt.split():  
            for j in i:
                sum=(((ord(j) -65) + k) % 26)
                ct=ct + (chr(sum +65))
                sum=0
            ct=ct + " "
        print("Cipher Text is: ",ct.lower())
    except:
        print("Something went wrong!")
        encryption2()
    display()
def decryption2():
    plt = ""
    ct = ciper_text()
    k = int(key())
    try:
        k=k % 26
        #if(k >= 1 and k <= 26):
        if(True):
            sum = 0
            for i in ct.split():  
                for j in i:
                    sum = (((ord(j) - 65) - k) % 26)
                    plt=plt + (chr(sum + 65))
                    sum = 0
                plt = plt + " "
            print("Plain Text is: ",plt.upper())
    except:
        print("Something went wrong!")
        decryption2()
    display()
def brute_force2():
    k = 0
    pt = plain_text()
    ct = ciper_text()
    try:
        while(chr(ord(pt[0]) + k) != ct[0]):
            k= k+1
        print("Key is:\t",k)
    except:
        print("Invalid text entered")
    display()
    
    
def encryption():
    ct = ""
    pt = plain_text()
    k = int(key())
    try:
        for i in pt.split():  
                for j in i:
                    sum=(((ord(j) - 65)*k) % 26)
                    ct=ct + (chr(sum + 65))
                    sum=0
                ct=ct + " "
        print("Cipher Text is: ",ct.lower())
    except:
        print("Something went wrong")
        encryption()
    display()
    
def modInverse() :
    a = int(key())
    a = a % 26; 
    for x in range(1, 26) : 
        if ((a * x) % 26 == 1) : 
            return x 
    return 1
def decryption():
    plt = ""
    ct = ciper_text()
    k = modInverse()
    
    try:
        k=k % 26
        #if(k >= 1 and k <= 26):
        if(True):
            sum = 0
            for i in ct.split():  
                for j in i:
                    sum = (((ord(j) - 65)*k) % 26)
                    plt=plt + (chr(sum +65))
                    sum = 0
                plt = plt + " "
            print("Plain Text is: ",plt.upper())
    except:
        print("Something went wrong")
        decryption()
    display()
def brute_force():
    print("Maybe, I will build this part in future!")
display()
