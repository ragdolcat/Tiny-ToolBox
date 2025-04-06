import zipfile
import zlib

#V1.0
#find a password to extract a zip file


def ZipCrackerMain():
    print("Hi, Welcome to Zipfile Cracker")

    lines = []
    
    while True:
        print("")
        secondInput = input(
            "What is your zip file named (format : [name].zip) ? ")
        try:
            foundedzip = zipfile.ZipFile("./" + secondInput)  # trying to import the zip file using user's first input
            print("zip file successfully imported")
            break
        except Exception:
            print("Cannot find your file")
            print("Make sure to put your file in the script Directory.")

    while True:
        print("")

        print("[1] 100 passwords")
        print("[2] 1 000 passwords")
        print("[3] 10 000 passwords")
        print("[4] 100 000 passwords")
        print("[5] choose your own list")
        print("")

        firstInput = input(
            "choose the number of passwords to test [1,2,3,4,5] : ")

        #with method is used to open the file, it will automatically close the file after the block is executed
        try:
            match firstInput:
                case "1":
                    with open("./list/100.txt", "r") as file:
                        lines = file.readlines()
                    break
                case "2":
                    with open("./list/1000.txt", "r") as file:
                        lines = file.readlines()
                    break
                case "3":
                    with open("./list/10000.txt", "r") as file:
                        lines = file.readlines()
                    break
                case "4":
                    with open("./list/100000.txt", "r") as file:
                        lines = file.readlines()
                    break
                case "5":
                    try:
                        print("")
                        thirdInput = input("What is your password list file named (example : dutchlist.txt) : ")
                        with open(thirdInput, "r") as file:  # trying to import custom list file using user's third input
                            lines = file.readlines()  # reading the file
                        break
                    except FileNotFoundError:
                        print("Cannot find your file")
                        print("Make sure to put your file in the 'list' Directory.")
                case _:
                    print("wrong input, please try again")
        except FileNotFoundError:
            print("Cannot find the file")
            print("Make sure to have the 'list' Directory with his content in the same folder as the script.")
        

    for line in lines:
        line = line.strip()  # remove the \n
        try:
            foundedzip.extractall("extract", pwd=bytes(line, 'utf-8'))  # trying to extract the zip file using the password
            print("")
            print("Password found:", line)
            print("files extracted in ./extract/[files]")
            break
        except zipfile.BadZipFile:
            print("The zip file is corrupted.")
            break
        except zipfile.LargeZipFile:
            print("The zip file is too large to be processed.")
            break
        except (RuntimeError, zlib.error):
            # RuntimeError is raised when the password is wrong
            print("wrong password, trying again...")
