import subprocess
from pyfiglet import Figlet
import pyzipper
from itertools import product
import string

title = Figlet(font='slant')
print(title.renderText('BrUtE-vAdEr'))

req = int(input("[+] Enter 0 for requirements > "))

if req == 0:
    subprocess.call("pip install pyfiglet", shell=True)
    subprocess.call("pip install pyzipper", shell=True)
else:
    print("-------Proceed-------")

print(("---------------------------------------------------------"))

print('1) Unzip using password wordlist')
print('2) Create a Wordlist')
cmd = int(input('[+] choose your task > '))

if cmd==1:
    wordlist = str(input('[+] Enter the wordlist location > '))
    file = str(input('[+] Enter the zip file location > '))
    content = str(input('[+] Enter the content in that file > '))
    print("Bruteforce Started.")

    fileobject = pyzipper.AESZipFile(file)

    with open(wordlist, "rb") as wordlist:
        for word in wordlist:
            try:
                fileobject.pwd = word.strip()
                fileobject.read(content)
            except:
                continue
            else:
                print("--------------------------*************---------------------------")
                print("Password Cracked > ", word.decode().strip())
                exit(0)
    print("No password found")
    print("...Task Completed...")
elif cmd == 2:
    cond = 1
    while cond == 1:
        print("-------------------------------------------------------------------")
        print("1) Numbers")
        print("2) Alphabets")
        print("3) Numbers with Alphabets")
        print("4) Alphabets with Special Charectors")
        print("5) No Choice")
        print("6) QUITT")
        print("-------------------------------------------------------------------")
        choice = int(input('[+] Enter your choice of password > '))
        if choice == 1:
            low = int(input('[+] Enter the minimum password length > '))
            high = int(input('[+] Enter the maximum password length > '))
            name = str(input("[+] Enter the wordlist name > "))
            counter = 0
            chars = string.digits
            myfile = open(name, "w+")
            for i in range(low, high):
                for j in product(chars, repeat=i):
                    word = "".join(j)
                    myfile.write(word)
                    myfile.write("\n")
                    counter = counter + 1
            print("Wordlist created successfully with ",counter ,"passwords")

        elif choice == 2:
            low = int(input('[+] Enter the minimum password length > '))
            high = int(input('[+] Enter the maximum password length > '))
            name = str(input("[+] Enter the wordlist name > "))
            counter = 0
            chars = string.ascii_lowercase + string.ascii_uppercase
            myfile = open(name, "w+")
            for i in range(low, high):
                for j in product(chars, repeat=i):
                    word = "".join(j)
                    myfile.write(word)
                    myfile.write("\n")
                    counter = counter + 1
            print("Wordlist created successfully with ",counter ,"passwords")

        elif choice == 3:
            low = int(input('[+] Enter the minimum password length > '))
            high = int(input('[+] Enter the maximum password length > '))
            name = str(input("[+] Enter the wordlist name > "))
            counter = 0
            chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
            myfile = open(name, "w+")
            for i in range(low, high):
                for j in product(chars, repeat=i):
                    word = "".join(j)
                    myfile.write(word)
                    myfile.write("\n")
                    counter = counter + 1
            print("Wordlist created successfully with ",counter ,"passwords")

        elif choice == 4:
            low = int(input('[+] Enter the minimum password length > '))
            high = int(input('[+] Enter the maximum password length > '))
            name = str(input("[+] Enter the wordlist name > "))
            counter = 0
            chars = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
            myfile = open(name, "w+")
            for i in range(low, high):
                for j in product(chars, repeat=i):
                    word = "".join(j)
                    myfile.write(word)
                    myfile.write("\n")
                    counter = counter + 1
            print("Wordlist created successfully with ",counter ,"passwords")

        elif choice == 5:
            low = int(input('[+] Enter the minimum password length > '))
            high = int(input('[+] Enter the maximum password length > '))
            name = str(input("[+] Enter the wordlist name > "))
            counter = 0
            chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
            myfile = open(name, "w+")
            for i in range(low, high):
                for j in product(chars, repeat=i):
                    word = "".join(j)
                    myfile.write(word)
                    myfile.write("\n")
                    counter = counter + 1
            print("Wordlist created successfully with ",counter ,"passwords")

        elif choice == 6:
            cond = cond + 1

        else:
            print("......Choose Wisely......")









