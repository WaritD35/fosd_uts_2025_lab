import math as m
import random

x = []

for i in range (1, 21):
    random_number = random.randrange(0, 100, 1)
    x.append(random_number)

print("Array x =", x)