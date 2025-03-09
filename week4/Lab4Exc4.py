x = []

n = int(input("n: "))
while n != -1:
    x.append(n)
    n = int(input("n: "))

print("minimum n =", min(x))
print("maximum n =", max(x))