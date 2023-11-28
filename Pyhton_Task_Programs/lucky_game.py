import random

lucky_num = random.randint(1, 100)
chances = 10

print("I've selected a random number between 1 and 100. You have 10 chances to guess it.")

while chances > 0:
    guess = int(input("Guess a number between 1 to 100: "))
    if guess == lucky_num:
        print("Congratulations! You guessed the correct number:", lucky_num)
        break
    elif guess < lucky_num:
        print("Hint: Think larger")
    else:
        print("Hint: Think smaller")
    chances -= 1
    print("Chances left:", chances)

if chances == 0:
    print("GAME OVER!!! The lucky number was:", lucky_num)

    play_again = input("Do you want to play again? ('Y / N') : ")
    if play_again.lower() == 'Y':
    # Start the game again
        lucky_num = random.randint(1, 100)
        chances = 10    
    else:
        print("Thanks for playing! Goodbye.")
