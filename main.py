'''
    Title: Customer Service Records, Calling and Statistics
    Author: Long Tieu and Wayne Seto
    Date: 26-10-2018
'''

from menu import *
from names import *
from call_customers import *
from customers_data import *

### --- Variables --- ###
names = []
served = []
left = []


### --- CODE STARTS HERE --- ###
while True:
    menu()
    option = chooseOptions()
    if (option == 1):
        takeNames(names)
    elif (option == 2):
        call_name(names, served)
    elif (option == 3):
        call_leave(names, left)
    elif (option == 4):
        ask_served(served)
    elif (option == 5):
        ask_left(left)
    elif (option == 6):
        print_list_served(served)
    elif (option == 7):
        print_list_left(left)
        
    again = input("Do you want to ask anything again? ")
    if (again == "y" or again "Y" or again == ""):
        pass
    else:
        break
        
        