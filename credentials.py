# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Cassady Czarnecki
# Created: 2020-04-22

first = input("Enter your first name: ")
last = input("Enter your last name: ")

def getname():
    return (first, last)
other = getname()
print(other)

uname = (first +"."+ last)
def username():
        print(uname.lower())

def strength():
    weak = "Password weak"
    strong = "Password strong"
    print("Please create a new password.")
    while True:
        passwd = input("Create a new password: ")
        if len(passwd) < 8:
            print("Fool of a Took! That password is feeble!")
            passwd = input("Create a new password: ")
        elif len(passwd) > 7:
            if all(char.islower() for char in passwd) or all(char.isupper() for char in passwd):
                print(weak)
                print("The force is strong in this one…")
            elif any(char.isupper () for char in passwd):
                print(strong)
                print("The force is strong in this one…")
        break
    print("Account configured. Your new email address is", uname + "@marist.edumain()") 


def main():
     getname()
     username()
     strength()

main()


        
