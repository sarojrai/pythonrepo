import random

hidden = random.randrange(1, 201)
# print hidden
print(hidden)

guess = int(raw_input("Please enter your guess: "))

if guess == hidden:
    print "Hit!"
elif guess < hidden:
    print "Your guess is too low"
else:
    print "Your guess is too high"