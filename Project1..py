# CMPT 120 Intro to Programming
# Project 2 - Game
# Author: Cassady Czarnecki
# Created: 2020-02-28

#Global List
description = ["It looks like your team has passed Mars!","You have arrived at the repair station and located the parts! Head back to the ship, repair, and get back in the race!","You have passed Jupiter and earned another 100 points!", "Your team has pulled ahead! You just passed Saturn and Uranus!","Press Enter to land on Earth!", "Congratulations! You made it to the space station and have won the race!" ]

def myFunc(food):
    print(food)

def locale0(description):
    print(description[0])

def locale1(description):
    print(description[1])

def locale2(description):
    print(description[2])

def com():
    n = ("north")
    s = ["south","west","east"]
    h = "y"
    qu = "quit"
    loc = "That is a good direction"
    question = input("Would you like to go North, South, East, and West?")
    c = ("Press Enter to continue...")
    while question != "north":
        print("Sorry that is the wrong direction. Try again.")
        question = (input("Would you like to go North, South, East, and West? Do you need help? Would you like to quit?"))
            
        if question == "north":
            break
    
    hel = input("Do you need help?")
    ff = "Woulf you like to quit?"
    while True:
        if hel == "yes":
            ff = input("Would you like to quit?")
            if ff == "yes":
                print("Game over")
            
            elif ff == "no":
                input(c)
                break
        elif hel == "no":
            input(c)
            break
 
            
def locale3(description):
    print(description[3])

def locale4(description):
    print(description[4])

def locale5(description):
    print(description[5])

locationscore = "Current location and score"
oo = "Your location is Mars and your score is 100."
op = "Your location is the repair station"
oi = "Your location is Jupiter and your score is 200."
ou = "Your location is just past Saturn and Uranus and your score is 400."
oy = "Your location is Earth"
ot = "Your location is the Space Station."
def currentls(locationscore):
    
    xx = print(locale0(description[0]))
    while True:
        if xx == (locale0(description)):
            print(oo)
            break
        elif xx == (locale1(description)):
            print(op)
            break
        else:
            xx == (locale2(description))
            print(oi)
            break
        if xx == (locale3(description)):
            print(ou)
            break
        elif xx == (locale4(description)):
            print(oy)
            break
        else:
            xx == (locale5(description))
            print(ot)
            break

def intro(intro):
    a = ("Welcome to A Space Adventure")
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

def ending(ending):
    print()
    print("Copyright Cassady Czarnecki 2020")
            
def main():
     
    intro(intro)
    print() # Prints a blank line
    score = 'Score:'
    print(score, 0)
    c = ("Press Enter to continue...")
    input(c)
    print()

    d = ("Congratulations for being a part of the race! We will be starting in 3, 2, 1...GO!")
    print(d)
    input(c)
    print()

    print(locale0(description))
    input(c)
    h = ("You have been awarded 100 points!")
    print(h)
    print(score, 0 + 100)
    print(oo)
    input(c)
    print()
    
    food = "Cheeseburger"
    q = ("You may stop for a food break which will be a...")
    print(q)
    myFunc(food)
    input(c)
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
    
    l = ("Your team must take a detour and find the nearest repair station! The closest one is 0.5 miles north!")
    print(l)
    input(c)
    print()
    print(locale1(description))
    print(op)
    input(c)
    print()
    
    g = ("Good job on fixing the issue! Only one team has managed to pass you! Go quick and you might be able to catch up!")
    print(g)
    input(c)
    com()
    print(locale2(description))
    print(score, 0 + 100 + 100)
    print (oi)
    input(c)
    print()

    y = ("Keep going you are tied with Team 2!")
    print(y)
    print(locale3(description))
    print(score, 0 + 100 + 100 +200)
    print(ou)
    input(c)
    print()
    
    q = ("The first team to land on Earth and arrive at the space station will win!")
    print(q)
    print(locale4(description))
    print(oy)
    print()

    zz = ("Quick run to the station, Team 2 is right behind you!")
    print(zz)
    zx = input("Press the Enter to run!")
    print(zx)
    print()
    print(locale5(description))
    print(ot)
    print()

    ending(ending)
    
    
main()

    


