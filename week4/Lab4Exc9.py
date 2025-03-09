import random

random_number = random.randint(1, 10)

while True:
    guess = int(input("Enter your guess number: "))
    if guess == random_number:
        print("Success, secret number =", random_number)
        break
    else:
        print("Sorry – try again!")