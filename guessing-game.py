def main():
    a = ("Python Guessing Game")
    print (a)

    c = ("dog")
    guess = (input("Guess an animal."))


    x = not c
    while guess != x:
        print ("Sorry, you guessed incorrectly. Try again. \n")
        guess = (input("Guess an animal."))

        if guess == c:
            print("Congratulations! You guess the animal!")
            break
main()
