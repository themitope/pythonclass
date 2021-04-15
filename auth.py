database = {}

import random
#Initializing the system
def init():
    print("Welcome to My Bank")
    haveAccount = int (raw_input("Do you have account with us: 1 (yes) 2 (no)"))
    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print("You have selected invalid option")
        init()

def login():
    print("***** Login ******")
    isloginSuccessful = False
    while isloginSuccessful == False:
        accountNumberFromUser = int(raw_input("What is your account number? \n"))
        password = raw_input("What is your password? \n")

        for accountNumber, userDetails in database.items():
            if(accountNumber == accountNumberFromUser):
                if(userDetails[3] == password):
                    isloginSuccessful = True
        print("Invalid account or password")
    bankOperation(userDetails)

def register():
    print("***** Register ******")
    email = raw_input("What is your email address? \n")
    first_name = raw_input("What is your first name? \n")
    last_name = raw_input("What is your last name? \n")
    password = raw_input("Create a password \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password]

    print("Your account has been created \n")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keepp it safe \n")

    login()

def bankOperation(user):
    print("Welcome %s %s" % (user[0], user[1]))
    selectedOption = int(raw_input("What would you like to do? (1)Deposit (2) Withdrawal (3) Logout (4) Exit"))
    if(selectedOption == 1):
        depositOperation()
    elif(selectedOption == 2):
        withdrawalOperation()
    elif(selectedOption == 3):
        login()
    elif(selectedOption == 4):
        exit()
    else:
        print("Invalid option selected")
        bankOperation(user)


def withdrawalOperation():
    print("withdrawal")

def depositOperation():
    print("Deposit")



def generationAccountNumber():
    return random.randrange(1111111111, 9999999999)

# ACTUAL BANKING SYSTEM
init()

