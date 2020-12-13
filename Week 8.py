import os.path



DIR_NAME = input("What is the directory name? ")
FILE_NAME = input("What is file name? ")

DIR_NAME_TEST = os.path.exists(DIR_NAME)

print(DIR_NAME_TEST)


if not os.path.exists("DIR_NAME_TEST"):
    try:
        os.makedirs("NEW_DIR")
    except OSError as e:
        print(e)

USERNAME = input("Enter your Name")
ADDRESS = input("Enter your address")
PH_NUM = input("Enter your phone number")

with open(FILE_NAME, 'w') as filehandle:
    fileHandle.write(USERNAME+", "+ADDRESS+", "+ PH_NUM)
