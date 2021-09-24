#The program allows a user to create, modify, or read a .txt file
#Created by: Chris Caponi

def main(): #The main function prompts the user for input and calls the writeIt or readIt function based on input
    action = input("Enter w to create a file, a to add data to a file, or r to read a file. ")
    fileName = input("What is the file name? ")
    while action not in ("w", "a", "r"):
        action = input("Enter w to create a file, a to add data to a file, or r to read a file. ")
    if (action == "w" or action =="a"):
        writeIt(fileName, action)
        print("Goodbye")
    else:
        readIt(fileName)

def writeIt(fileName, action): #The writeIt function is used to create a new file or modify an existing file (action = "w", "a")
    fileOut = open(fileName, action)
    for x in range(3):
        name = input("Give me a name.  ")
        fileOut.write(name+'\n')

def readIt(fileName): #The readIt function reads through an existing file (action = "r")
    fileIn = open(fileName, 'r')
    name = fileIn.readline()
    while name != '':
        name = name.rstrip('\n')
        print(name)
        name = fileIn.readline()
    fileIn.close()
main()

         