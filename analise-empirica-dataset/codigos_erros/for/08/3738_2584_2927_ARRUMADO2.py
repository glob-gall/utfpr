N = int(input("Digite o valor de N: "))
H = 0.0

for i in range(1, N + 1):
    if i % 2 == 0:
        H -= 1 / i
    else:
        H += 1 / i

print("H =", round(H, 6))
