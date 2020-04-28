def main():
    x = ("Hello! Welcome to my interactive dictionary!")
    print(x)
    
    while True:
        word = input("Enter a word: ")
        print(word)
        with open("dictionary.txt", "r") as myFile:
            lines = myFile.readlines()
            lines = [wrd.strip() for wrd in lines]
            
        if word == lines[0]:
            print(lines[1])
            
        if word == lines[2]:
            print(lines[3])
            
        if word == lines[4]:
            print(lines[5])
            
        if word == "":
            print("sorry that is not a word")
            quit()
            
        if word not in lines and not "":
            print("That word does not exist, try again. \n")
            

main()
