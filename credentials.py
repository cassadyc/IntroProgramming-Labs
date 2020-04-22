# CMPT 120 Intro to Programming
# Lab #5 – Working with Strings and Functions
# Author: Cassady Czarnecki
# Created: 2020-04-22

def main():
    # get user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")

    # TODO modify this to generate a Marist-style username
    uname = (first + "." + last)
    print(uname)

    # TODO modify this to ensure the password has at least 8 characters
    print("Please create a new password.")
    while True:
        passwd = input("Create a new password: ")
        if len(passwd) < 8:
            print("Fool of a Took! That password is feeble!")
            passwd = input("Create a new password: ")
        if len(passwd) > 7:
            print("The force is strong in this one…")
            break
    print("Account configured. Your new email address is", uname + "@marist.edu")
    

main()
