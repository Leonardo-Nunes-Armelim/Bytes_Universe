import random

play = True
sort = True


while play:

    if sort == True:
        number = random.randint(1, 10)
        sort = False
        print("Guess the number I'm thinking of...")
    
    guess = int(input("Response: "))

    if guess == number:
        print("That's right, you got it right!")
        replay = input('Want to play again? (yes/no)\nResponse: ')
        if replay == "yes":
            sort = True
        else:
            play = False
    elif guess < number:
        print("No, the number I'm thinking of is higher")
    else:
        print("No, the number I'm thinking of is smaller")
