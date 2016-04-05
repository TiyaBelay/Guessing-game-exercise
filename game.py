# Put your code here
from random import randint

greeting = raw_input("Hello, what is your name? ")

player_guesses = []
comp_guesses = randint(1,100)

print "%s, I'm thinking of a number between 1 and 100." % (greeting)
player_prompt = int(raw_input("Try to guess my number. "))

# while True:
