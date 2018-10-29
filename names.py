

def takeNames(names):
    play = True
    while play:
        enter_name = input("Please enter your name: ")
        names.append(enter_name)
        enter_name_again = input("Do you want to put more names? y/n ")
        if enter_name_again == "y":
            pass
        else:
            play = False

takeNames(names)
print(names)