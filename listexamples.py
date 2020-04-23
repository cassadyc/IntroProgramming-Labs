color = "RED", "ORANGE", "YELLOW"

def showTitle():
    print("Color Preference Evaluator")

def promptFORCOLOR():
    global qt
    qt = input("Type a color name").upper().strip()
        
def confirmCOLOR():
    c = print("You entered ", qt)
    z = input("Is this correct? y/n?")
    while True:
        if z == "y":
            print("TRUE")
            break
        elif z == "n":
            main()

def containsElement():
    while True:
        if qt == color[0]:
            praiseUser()
            break
        else:
            ridiculeUser()
            break

def praiseUser():
    print("Congratulations that is the correct color!")

def ridiculeUser():
    print("Sorry, that was not the color.")

def main():

    z = showTitle()
    y = promptFORCOLOR()
    x =confirmCOLOR()
    w = containsElement()
    

main()
