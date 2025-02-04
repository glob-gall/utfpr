n = int(input("Digite o número de termos da série: "))
d = 0

for i in range(1, n + 1):
    s = (-1) ** (i + 1)
    d += s / i

print("H =", round(d, 6))
