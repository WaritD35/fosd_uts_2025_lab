n = int(input("Enter a number: "))

while n != -1:
    if n % 2 != 0:
        n -= 1

    sum = 0
    for i in range(2, n+2, 2):
        sum += i
    print("sum of even number from 1 to n =", sum)
    n = int(input("Enter a number: "))