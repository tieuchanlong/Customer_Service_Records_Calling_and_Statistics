'''
    This is the call name and check leaving sutomers file.
'''

def call_name(names, served):
    print("The next person is " + names[0] + ".")
    served.append(names.pop(0))
    
def call_leave(names, left):
    customer_name = input("The name of the customer who wants to leave:  ")
    for i in range(0, len(names) - 1):
        if (names[i] == customer_name):
            left.append(names.pop(i))
            break
        
        
    
    