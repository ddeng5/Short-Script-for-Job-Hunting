import sys
import os
from random import randint


os.system('cls' if os.name == 'nt' else 'clear')
loggedIn = True


#this is the main menu selection for the question bank
def mainMenu():
    print("Welcome to the Investment Banking Question Bank: ")
    print("")
    print("")
    print("Which area would you like you like to be tested on: ")
    print("     1. Understanding banking and suggested answers")

    print("")
    print("TYPE q AT ANYTIME TO EXIT THE QUESTION BANK")
    print("")
    print("")
    category = input("Enter a number: ")
    return category



def understandingBanking():
    #generate random question number
    qNum = 1

    if qNum == 1:
        print("")
        print("You have never worked in finance before. How much do you know about what bankers actually do?")
        #ask the user if they would like to see the answer
        choice = raw_input("Would you like to see the answer (y/n)?")
        if (choice == "y"):
            print("")
            print("Acknowledge that you haven't worked in the field before but you've done your research and you've talked to people in the industry.")
            print("Bankers advise companies on transactions - buying, selling companies and raising capital. Day-to-day work includes creating presentations, financial analysis and marketing material such as Executive Summaries.")
            print("")
            print("")
            print("")
            
        #press any button to continue
        raw_input("Press any button to continue")



while (loggedIn):
    #clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    category = mainMenu()

    #check if the user is exiting
    if category == "q":
        loggedIn = False
        print ("You are now exiting the question bank. Good luck on your interviews!")

    else:
        #questions for Understanding Banking
        if category == 1:
            understandingBanking()
