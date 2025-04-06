import lib

import lib.ZipCracker
import lib.PwdGen
import lib.BruteForce

## tiny tool box
# this is a simple tool box for some useful tools 

def main():
    programbool = True

    print("")
    print("hi, Welcome to tiny tool box")

    while programbool:
        print("")

        print("[1] simple password generator")
        print("[2] Brute force password generator")
        print("[3] zip file cracker")
        print("")        
        
        userInput = input("choose any action  [1,2,3 or x for exit] : ")
        print("")
        
        # match the user input with the available options
        match userInput:
            case "1":
                # call mainPwdGen() from lib/PwdGen.py
                lib.PwdGen.mainPwdGen()
            case "2":
                # call mainBruteForce() from lib/BruteForce.py
                lib.BruteForce.mainBruteForce()
            case "3":
                # call ZipCrackerMain() from lib/ZipCracker.py
                lib.ZipCracker.ZipCrackerMain()
            case "x":
                programbool = False
                print("Thank you for using the tiny tool box")
                break
            case _:
                print("wrong input, please try again")

           
# execute the main function as a standalone program or as a imported module

if __name__ == "__main__":
    main()