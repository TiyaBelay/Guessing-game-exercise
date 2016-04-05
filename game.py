# Put your code here
from random import randint

greeting = raw_input("Hello, what is your name? ")



def guessing_game():
    guesses = []
    comp_guess = randint(1,100)

    print "%s, I'm thinking of a number between 1 and 100." % (greeting)
    while True:
        try:
            player_guess = int(raw_input("Try to guess my number. "))
        except:
            print ("That's not a number. Try again")
            continue

        if player_guess < 1 or player_guess > 100:
            print "GUESS DENIED!! Enter a valid number." 
            continue 
            
        guesses.append(player_guess)

        if player_guess == comp_guess:
            print "Congratulations, %s! You found my number in %s tries!" % (greeting, len(guesses))
            break

        elif player_guess > comp_guess:
            print "Your guess is too high. try again!"
        elif player_guess < comp_guess:
            print "Your guess is too low. try again!"

guessing_game()


while True: 
    play_again = raw_input("Would you like to play again? ")
    if play_again == "y":
        guessing_game()
    elif play_again == "n":
        break