n = int(input('n = '))

fibo1 = 1
fibo2 = 1

print(fibo1)

while (fibo2 < n):
    fibo_next = fibo1 + fibo2
    fibo1 = fibo2
    fibo2 = fibo_next
    print(fibo1)
