import random

def random_number():
    rand = []
    for i in range(5):
        x = random.randint(1, 10)
        rand.append(x)
    print(rand)
    return rand

# # takes a number
def factorial(a):
    fact = 1
    for i in range(1, a+1):
        fact = fact * i
    print(fact)
    return fact

# takes a list of numbers
def factorial(numbers):
    fact = []
    for i in numbers:
        f = 1
        for j in range(1, i+1):
            f = f * j
        fact.append(f)
    print(fact)
    return fact

# Test
x = random_number()
factorial(x)