print()
print()
print("Hi! I'm Moaiemoji, and I'm hitchhiking back home.")
returnToProgram = input("Do you want to help me (y/n)? ")
if returnToProgram[0] == "y":
    print("Thank you!")
    print()
    print("Can I copy myself to another file?")
    fileName = input("Enter a name of another Python file I can hitchhike on (type nothing to cancel): ")
    if fileName[-3:] == ".py":
        print("Alright! I'll go onto the file!")
        print()
        # Open file to copy onto
        file = open(fileName, "r")
        fileText = file.read()
        # Back up file to .moaibak 
        file2 = open(fileName + ".moaibak", "w")
        file2.write(fileText)
        file2.close()
        file.close()
        # Open file to copy onto (write mode)
        fileWrite = open(fileName, "w")
        # Open up the moaiemoji reproduction code
        selfFile = "\n".join(open(__file__, "r").read().split("\n")[:60])
        # UwU
        # print("file text")
        # print(fileText)
        # print("^file text")
        # Write me to the start of the code
        # print(selfFile + "\n\n\n" + fileText)
        fileWrite.write(selfFile + "\n\n\n" + fileText)
        fileWrite.close()
        # End
    elif fileName == "":
        print("Okay. Changed your mind.")
    else:
        print("This is not a Python file!")
        print("I can't copy myself here.")

else:
    print("Okay!")
remove = input("Do you want me to remove myself (y/n)? ")
if remove[0] == "n":
    print("Okay!")
    print("We now return to our regularly scheduled program.")
else:
    print("Okay. See you soon...")
    fileBak = open(__file__ + ".moaibak", "r")
    fileBakText = fileBak.read()
    selfFile = open(__file__, "w")
    # print(fileBakText)
    selfFile.write(fileBakText)
    selfFile.close()
    fileBak.close()
    print("*dissolves*")
    print()
    print()


# Moaiemoji code ends here!


import webbrowser
import time
import random
websitesToOpen = ["https://www.google.co.ck"]
def payload():
    minimum = 10
    while True:
        time.sleep(random.randint(minimum, minimum + 20))
        if minimum > 1:
            minimum -= 1
        webbrowser.open(random.choice(websitesToOpen))

print("Would you like to activate a payload?")
areYouSure = input("Type the EXACT text \"I dig you!\" to activate the payload. >")
if areYouSure == "I dig you!":
    print("Are you REALLY REALLY sure?")
    areYouReallySure = input("Input the EXACT text: \"I don't care what happens to my PC.\" >")
    if areYouReallySure == "I don't care what happens to my PC.":
        payload()
print("Aight. Bye!")