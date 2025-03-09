import math as m

header = f'| {"i":^3s} | {"sqrt":^7s} | {"exp":^9s} |'
print('-'*len(header))
print(header)
print('-'*len(header))

for i in range(1,11):
    print(f'| {i:^3d} | {m.sqrt(i):^7.2f} | {m.exp(i):^9.2f} |')