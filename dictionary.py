def main():
    x = ("Hello! Welcome to my interactive dictionary!")
    print(x)
    
    while True:
        word = input("Enter a word: ")
        print(word)
        with open("dictionary.txt", "r") as myFile:
            lines = myFile.readlines()
            dicti = {1: 'box', 2: 'car', 3: 'train'}
            
        if word == dicti[1]:
            print(lines[1])
            
        if word == dicti[2]:
            print(lines[3])
            
        if word == dicti[3]:
            print(lines[5])
            
        if word == "":
            print("sorry that is not a word")
            quit()
            
        if word not in dicti and not "":
            print("That word does not exist, try again. \n")
            

main()
