import random

def passwordGenerator(passwordLength, numberOfSpecialChars, numberOfNumbers):

  # V1.0 - Initial version (2023-10-01)
  # This script generates a random password based on user-defined criteria.
  #Generation of a random password according to 3 criteria
  #1. Length of the password (passwordLength)
  #2. Number of special characters (numberOfSpecialChars)
  #3. Number of digits (numberOfNumbers)

  charAlph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  charNum = "0123456789"
  charSpecial = "!@#$%^&*()_+-?~'"

  password = ""

  #generation of the number of special characters and digits in the password
  if numberOfSpecialChars == 0:
     shuffledNumberOfNumbers  = 0
  else:
    shuffledNumberOfNumbers = random.randint(numberOfNumbers, passwordLength // 3)
    
  if numberOfSpecialChars  == 0:
     shuffledNumberOfSpecialChars   = 0
  else:
    shuffledNumberOfSpecialChars = random.randint(numberOfSpecialChars, passwordLength // 3)

  #generation of the password
  for i in range(shuffledNumberOfNumbers): 
    password += charNum[random.randint(0,len(charNum) - 1)]  #-1 to avoid index out of range
    
  for i in range(shuffledNumberOfSpecialChars): 
    password += charSpecial[random.randint(0,len(charSpecial) - 1)]  #-1 to avoid index out of range
    
  for i in range(passwordLength - shuffledNumberOfNumbers - shuffledNumberOfSpecialChars):
    password += charAlph[random.randint(0,len(charAlph) - 1)]  #-1 to avoid index out of range
  
  # Convert the password string into a list of characters
  password = list(password)  
  
  # Shuffle the password to make it more random
  random.shuffle(password)  
  
  # Convert the list of characters back into a string and return it
  return ''.join(password)


def mainPwdGen():
  
  passwordLength = 0
  numberOfSpecialChars = 0
  numberOfNumbers = 0
  password = ""
  
  print("Hi, Welcome to Password Generator")
  
  # loop for the length of the password
  while True: 
    
    print("")
    passwordLength = input("What is the length of your password ? ")
    
    try:
      passwordLength = int(passwordLength)
      if passwordLength < 1:
        print("Please enter a number greater than 0")
        continue
      break
    except ValueError:
      print("Please enter a number greater than 0")
  
  # special characters loop 
  while True:  
    
    print("")
    numberOfSpecialChars = input("How many special characters do you want at minimum in your password ? ")
    
    try:
      numberOfSpecialChars = int(numberOfSpecialChars)
      if numberOfSpecialChars < 0 or numberOfSpecialChars > passwordLength:
        print("Please enter a number between 0 and ", passwordLength)
        continue
      break
    except ValueError:
      print("Please enter a number between 0 and ", passwordLength)
  
  # numbers loop
  while True:  
    
    print("")
    numberOfNumbers = input("How many numbers do you want at minimum in your password ? ")
    
    try:
      numberOfNumbers = int(numberOfNumbers)
      if numberOfNumbers < 0 or numberOfNumbers > passwordLength:
        print("Please enter a number between 0 and ", passwordLength)
        continue
      break
    except ValueError:
      print("Please enter a number between 0 and ", passwordLength)
  
  # loop for the generation of the password
  while True: 
     
    print("")
    UserInput = input("Do you want to generate a password ? [y/n] ")
    
    if UserInput.lower() in ["y", ""]:
      password = passwordGenerator(passwordLength, numberOfSpecialChars,numberOfNumbers)
      print("")
      print("Your password is : ", password)
      break
    elif UserInput.lower() == "n":
      print("Goodbye")
      break
    else:
      print("Invalid input. Please enter 'y' or 'n'")