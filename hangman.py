import random  # Importing the random module
print("********** Hangman Game! **********")  # Printing a banner for the game
word_bank = ["apple", "banana", "chocolate", "elephant", "guitar", "house", "jungle", "kangaroo", "lion", "mountain", "ocean", "piano", "rabbit", "sunflower", "tiger", "umbrella", "violin", "watermelon", "xylophone", "zebra"]  # List of words for the game
word = word_bank[random.randint(1,len(word_bank))]  # Randomly selecting a word from the word bank
n = len(word)  # Determining the length of the selected word
spaces = []  # Creating a list to store the guessed letters and underscores
for i in range(n):  # Iterating through each character in the word
    spaces.append("_")  # Adding underscores for each character to the spaces list
life = 3  # Setting the initial number of lives
game_over = False  # Flag to check if the game is over
while game_over!=True:  # Loop until the game is over
    guess = ""  # Initializing an empty string to store the current guess
    for i in spaces:  # Looping through the spaces list to form the current guess
        guess += i  # Adding each character to the guess string
    if guess != word:  # Checking if the guess is not equal to the word
        if life==0:  # Checking if the player has run out of lives
            print("Insufficient Life!")  # Printing a message for insufficient life
            game_over = True  # Setting the game_over flag to True
        else:
            for i in spaces:  # Looping through the spaces list to display the current state of the word
                print(i,end=" ")  # Printing each character or underscore with a space
            print()  # Printing a newline
            temp = input("Enter Guess: ").lower()  # Asking the player for a guess and converting it to lowercase
            if temp in guess:  # Checking if the guess has already been made
                life -= 1  # Decreasing the number of lives
                print(f"Already Guessed! Life Remaining: {life}")  # Informing the player about the duplicate guess
            elif temp in word:  # Checking if the guess is correct
                for i in range(n):  # Iterating through each character in the word
                    if word[i] == temp:  # Checking if the character matches the guess
                        spaces[i] = temp  # Updating the spaces list with the correct guess
            else:  # If the guess is incorrect
                life-=1  # Decreasing the number of lives
                print(f"Oops Wrong Guess! Life Remaining: {life}")  # Informing the player about the wrong guess
    else:  # If the guess matches the word
        print(word)  # Printing the word
        print("Bravo You Won!")  # Congratulating the player for winning
        game_over = True  # Setting the game_over flag to True
