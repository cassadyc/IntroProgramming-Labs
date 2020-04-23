# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Cassady Czarnecki
# Created: 2020-04-22

first = input("Enter your first name: ")
last = input("Enter your last name: ")
def getname():
    return (first, last);
list = getname()
print(list)


uname = (first +"."+ last)
def username():
        print(uname)


def password():
        print("Please create a new password.")
        while True:
            passwd = input("Create a new password: ")
            if len(passwd) < 8:
                print("Fool of a Took! That password is feeble!")
                passwd = input("Create a new password: ")
            if len(passwd) > 7:
                print("The force is strong in this one…")
                break
        print("Account configured. Your new email address is", uname + "@marist.edumain()") 


def main():
     getname()
     username()
     password()

main()


        
