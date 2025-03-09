import random

n = int(input("Enter the number of random numbers to generate: "))
random.seed(10)

sum = 0
for i in range(n):
    x = random.randint(1, 100)

    if x % 2 == 0:
        sum += x


print("total sum of even numbers is: ", sum)
