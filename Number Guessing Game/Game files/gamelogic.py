import random



def gamefunc(playerInput):
    randomNumber = random.randint(1, 50)
    if randomNumber == playerInput:
        print("Congratulations! You have won by guessing the number correct!")
    else:
        message = input("OOPS! You guessed it wrong! Type 'again' to retry or 'quit' to quit the game")
        while message.lower() == 'again' or message.lower() == 'quit':
            if message.lower() == 'again':
                question = input("Guess a number from 1 to 50 !!")
                gamefunc(question)
            elif message.lower() == 'quit':
                print("BYE BYE !!")
                break
        else:
            while message.lower() != 'quit' or message.lower() != 'again':
                message = input("Please type 'again' to retry or 'quit' to quit the game")
                if message.lower() == 'again':
                    question = input("Guess a number from 1 to 50 !!")
                    gamefunc(question)
                elif message.lower() == 'quit':
                    print("BYE BYE !!")
                    break

