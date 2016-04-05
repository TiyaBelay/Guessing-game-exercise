# Put your code here
from random import randint

greeting = raw_input("Hello, what is your name? ")

guesses = []
comp_guess = randint(1,100)

print "%s, I'm thinking of a number between 1 and 100." % (greeting)


while True:
    player_guess = int(raw_input("Try to guess my number. "))

    guesses.append(player_guess)

    if player_guess == comp_guess:
        print "Congratulations, %s! You found my number in %s tries!" % (greeting, len(guesses))
        break
    elif player_guess > comp_guess:
        print "Your guess is too high. try again!"
    elif player_guess < comp_guess:
        print "Your guess is too low. try again!"     