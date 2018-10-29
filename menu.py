# 1 and 2
import time

def menu():
    # intro #
    print("Welcome to Customer Service Records!")
    time.sleep(2)
    print("")
    print("Please tell us your option or what you wish to do!")
    time.sleep(2)
    print("")

def chooseOptions():

    # Choose options #
    print("""
    1.) Queue for the customer service by providing us your name
    2.) Ask for the next person's name
    3.) Ask for a permit to leave
    4.) Ask for the number of customers that have been served
    5.) Ask for the number of customers that have left
    6.) Ask for the list of customer that have been served
    7.) Ask for the list of custoner that haven't been served
    """)
    options = int(input("Your choice? : "))
    return options





