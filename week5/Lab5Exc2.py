import random
import math

def random_number():
    rand = []
    for i in range(20):
        x = random.randint(1, 100)
        rand.append(x)
    return rand

def cal_mean(x):
    mean = sum(x) / len(x)
    return mean

def cal_std(x):
    mean = cal_mean(x)
    std = 0
    for i in x:
        std += (i - mean)**2
    std = std / len(x)
    std = math.sqrt(std)

    return float("{:.2f}".format(std))

# Test
x = random_number()
print(x)
print(cal_mean(x))
print(cal_std(x))