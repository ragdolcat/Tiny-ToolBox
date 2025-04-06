import zipfile


def bruteforcePassword(alphabet, length, prefix=""):
  # V1.0
  # write a list of brute force a password

  file = open("./extract/pwd.txt", "w")

  if length == 0:
    return [prefix]  # return the password

  words = []
  words += [prefix]  # return password under the wanted length

  for i in alphabet:
    words += bruteforcePassword(alphabet, length - 1,prefix + i)  # recursive call
    file.write(" ".join([prefix]))

  file.close()
  return words


def mainBruteForce():

  alphabet = "abcdefghijklmnopqrstuvwxyz"
  uppercaseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  numbers = "0123456789"
  specialCharacters = "!@#$%^&*()_+-?~'"

  finalList = ""  # Holds the combined characters the user selected
  chosenList = 0  # Tracks how many lists the user selected
  
  testOnZip = False
  zipPwdfinded = True

  print("Hi, Welcome to the brutforcer password generator version :3")
  
  # characters list selection loop
  while True:

    print("")
      
    print("[1] ", alphabet)
    print("[2] ", uppercaseAlphabet)
    print("[3] ", numbers)
    print("[4] ", specialCharacters)
    print("")

    userInput = input("Choose one of the list for the generated list (n to skip): ")
      
    match userInput:
      case "1":
        chosenList += 1
        finalList += alphabet
        print(" list 1 successfully added")
      case "2":
        chosenList += 1
        finalList += uppercaseAlphabet
        print("list 2 successfully added")
      case "3":
        chosenList += 1
        finalList += numbers
        print("list 3 successfully added")
      case "4":
        finalList += specialCharacters
        print("list 4 successfully added")
      case "n":
        if chosenList == 0:
          print("Please choose at least one list")
          continue
        else:
          print("No more list to add")
          break
      case _:
        print("wrong input, please try again")


    #asking the user if he want to add another list
    
    userInput = input("Do you want to add another list ? [y/n] ")

    if userInput.lower() in ["yes","y",""]:  
      
      #checking the number of list added   
         
      if chosenList > 2:
        
        print("Adding to much list will will add a lot of computing time.")
        userInput = input("Do you realy want to continue ? [y/n] ")
        
        if userInput.lower() in ["y","yes", ""]:
          print("Adding another list...")
        else:
          break
    else:
      break

  # password length selection loop
  while True:
    
    print("")
    
    while True:  
      try:
        maxLength = int(input("Choose the maximum lenght of the password wanted : "))
        break
      except ValueError:
        print("Please only use number")

    # checking the length of the password 
    if maxLength >= 6 or chosenList > 1 and maxLength > 4:  

      print("Warning : choose a lenght of ", maxLength," will add a lot of computing time.")
      userInput = input("Do you realy want to continue ? ")

      if userInput.lower() in ["y","yes", ""]:
        break
    else:
      break
  
  # password generation loop
  while True:  
    print("")
    UserInput = input("Do you want to generate the password list ? [y/n] ")
    if UserInput.lower() in ["y", "yes", ""]:
      print("generating passwords...")
      
      file = open("./extract/pwd.txt","w")  # open the file to write the passwords
      listpwd = bruteforcePassword(finalList,maxLength)  # generating the list of passwords
      file.write("\n".join(listpwd))  # writing the list of passwords in a file
      file.close()

      pwdgenerated = True
      print("passwords Successfully generated in ./extract/pwd.txt")
      break
    elif UserInput == "n":
      pwdgenerated = False
      break
    else:
      print("Please enter y or n")

  while pwdgenerated:
    
    print("")
    
    confirmation = input("Do you want to use the generated passwords on a zip file? [y/n] ")
    
    if confirmation.lower() in ["y", "yes", ""]:
      zipPwdfinded = False
      testOnZip = True
      break
    elif confirmation.lower() in ["n", "no"]:
      break
    else:
      print("Please enter y or n")
      continue

  if testOnZip:
    
    # with method is used to open the file, it will automatically close the file after the block is executed
    
    with open("./extract/pwd.txt", "r") as file: # open the file to read the passwords
      lines = file.readlines()

    while True:
      print("")
      userInput = input("What is your zip file named (format : [name].zip) ? ")
      try:
        foundedzip = zipfile.ZipFile("../" + userInput)  # trying to import the zip file using user's first input
        print("zip file succesfully imported")
        break
      except ():
        print("Cannot find your file")
        print("Make shure to put your file in the script Directory.")
          
    for line in lines:
      line = line.strip()  # remove the \n
      try:
        foundedzip.extractall("extract", pwd=bytes(line,'utf-8'))  # try to extract the zip file using the password
        
        # if the password is correct, the zip file will be extracted
        zipPwdfinded = True
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
      except RuntimeError:
        print("wrong password, trying again...")
    
  if not zipPwdfinded:
    
    print("No password were found in the list")
    print("Please try again with a bigger list or a smaller list of passwords")
  else:
    print("")
    print("Thank you for using the bruteforcer password generator")
