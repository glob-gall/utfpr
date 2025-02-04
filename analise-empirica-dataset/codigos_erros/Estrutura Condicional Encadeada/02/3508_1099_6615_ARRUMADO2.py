L1 = float(input("Digite o comprimento de um lado: "))
L2 = float(input("Digite o comprimento de outro lado: "))
L3 = float(input("Digite o comprimento de mais um lado: "))
print("Entradas:", L1, ",", L2, ",", L3)

if L1 <= 0 or L2 <= 0 or L3 <= 0 or L1 + L2 <= L3 or L1 + L3 <= L2 or L2 + L3 <= L1:
    print("Tipo de triângulo: inválido")
elif L1 == L2 == L3:
    print("Tipo de triângulo: equilátero")
elif L1 == L2 or L1 == L3 or L2 == L3:
    print("Tipo de triângulo: isósceles")
else:
    print("Tipo de triângulo: escaleno")
