# CMPT 120 Intro to Programming
# Project 2 - Game
# Author: Cassady Czarnecki
# Created: 2020-02-28

#Global Lists
locNames = ["Mars","Repair Station","Jupiter","Saturn and Uranus","Earth","Space Station"]
description = ["It looks like your team has passed Mars!","You have arrived at the repair station and located the parts! Head back to the ship, repair, and get back in the race!","You have passed Jupiter and earned another 100 points!", "Your team has pulled ahead! You just passed Saturn and Uranus!","Press Enter to land on Earth!", "Congratulations! You made it to the space station and have won the race!" ]


hasBeen = ["False", "False", "False", "False", "False", "False"]

score = 'Score:'
locationscore = "Current location and score"
moves = 'Moves:'
numberMoves = 0
timeLimit = '12 moves'
c = ("Press Enter to continue...")

def timelimit():
    while True:
        if numberMoves == (12):
            quit()

def myFunc(food):
    print(food)

def locale0(description):
    print(locationscore)
    print("location:", locNames[0])
    if hasBeen[0]:
        print(score, 0 +100)
        print(description[0])
        hasBeen[0] = True
    if not hasBeen[0]:
        print("You have already been here, no points awarded.")
    input(c)
    print(moves, numberMoves + 2)
    print()
    food = "Cheeseburger"
    q = ("You may stop for a food break which will be a...")
    print(q)
    myFunc(food)
    input(c)
    print(moves, numberMoves + 3)
    print()
    v = ("I hope you enjoyed your break because now its time to get back to the race!")
    print(v)
    input(c)
    print()
    f = ("Oh no! There was a issue with your teams engine. You must land on Jupiter and repair the damage.")
    print(f)
    ff = ("Press Enter to inspect the damage.")
    input(ff)
    fd = ("Looks like you will need a new part")
    print(fd)
    input(c)
    print(moves, numberMoves + 4)
    print()
    l = ("Your team must take a detour and find the nearest repair station! The closest one is 0.5 miles")
    print(l)
    com()
    input(c)
    print()
    
def locale1(description):
    print(locationscore)
    print("location:", locNames[1])
    if hasBeen[1]:
        print(score, 0 +100)
        print(description[1])
        hasBeen[1] = True
    if not hasBeen[1]:
        print("You have already been here, no points awarded.")
    input(c)
    print(moves, numberMoves + 5)
    print()
    g = ("Good job on fixing the issue! Only one team has managed to pass you! Go quick and you might be able to catch up!")
    print(g)
    input(c)
    print(moves, numberMoves + 6)

def locale2(description):
    print(locationscore)
    print("location:", locNames[2])
    if hasBeen[2]:
        print(score, 0 + 100 + 100)
        print(description[2])
        hasBeen[2] = True
    if not hasBeen[2]:
        print("You have already been here, no points awarded.")
    input(c)
    print(moves, numberMoves + 7)
    print()
    y = ("Keep going you are tied with Team 2!")
    print(y)
 
def locale3(description):
    print(locationscore)
    print("location:", locNames[3])
    if hasBeen[3]:
        print(score, 0 + 100 + 100 + 200)
        print(description[3])
        hasBeen[3] = True
    if not hasBeen[3]:
        print("You have already been here, no points awarded.")
    print(moves, numberMoves + 8)
    input(c)
    print("Oh no! You need another part, make a quick trip back to the Reapair Station!")
    input("Press enter to go back to the Repair Station.")
    print("You have arrived at the repair station and located the parts! Head back to the ship, repair, and get back in the race!")
    print("No extra points awarded for going to the same location.")
    print(moves, numberMoves + 9)
    input(c)
    print()
    q = ("The first team to land on Earth and arrive at the space station will win!")
    print(q)

def locale4(description):
    print(locationscore)
    print("location:", locNames[4])
    if hasBeen[4]:
        print(score, 0 + 100 + 100 + 200)
        print(description[4])
        hasBeen[4] = True
    if not hasBeen[4]:
        print("You have already been here, no points awarded.")
    print(c)
    print(moves, numberMoves + 10)
    print()
    zz = ("Quick run to the station, Team 2 is right behind you!")
    print(zz)
    zx = input("Press the Enter to run!")
    print(zx)
    print(moves, numberMoves + 11)
    print()

def locale5(description):
    print(locationscore)
    print("location:", locNames[5])
    if hasBeen[5]:
        print(score, 0 + 100 + 100 + 200)
        print(description[5])
        hasBeen[5] = True
    if not hasBeen[5]:
        print("You have already been here, no points awarded.")
    print()
    input("Press enter to continue on")
    print(moves, numberMoves + 12)


def com():
    while True:
        command = input("Please enter command.")
        command = command.lower()
        if command in ["north", "south", "east", "west"]:
            if command == "north":
                locale1(description)
            elif command == "south":
                locale0(description)
            else:
                command == "east"
                locale0(description)
            if command == "west":
                locale0(description)
            break
        elif command == "help":
            he = input("Would you like to quit?")
            print(he)
            if he == "yes":
                print("Game Over")
                quit()      
            elif he == "no":
                print ("Continue on")
                break
        elif command == "quit":
            print ("Game Over")
            quit()
        
def intro():
    a = ("Welcome to A Space Adventure")
    c = ("Press Enter to continue...")
    print(a)
    print()
    introduction = "This game is a race through space!"
    print(introduction)
    print()
    b = ("Today you will be racing past the planets! For every planet you reach you will recieve 100 points. To win you must get 400 points. Your team is 1. To start the race please go to your ship in the basement.")
    print (b)
    print()
    name = input("Enter your team name")
    print(name)
    charac = input("Enter a one-word characteristic")
    print(charac)
    print(c)
    print() # Prints a blank line
    print(score, 0)
    print(moves, numberMoves)
    input(c)
    print()
    d = ("Congratulations for being a part of the race! We will be starting in 3, 2, 1...GO!")
    print(d)
    input(c)
    print(moves, numberMoves + 1)
    print()

def ending(ending):
    print()
    print("Copyright Cassady Czarnecki 2020")
            
def main():
    intro()
    locale0(description)
    locale1(description)
    locale2(description)
    locale3(description)
    locale4(description)
    locale5(description)
    ending(ending)
    
    
main()

    


