a = float(input("Digite o primeiro lado do triângulo: "))
b = float(input("Digite o segundo lado do triângulo: "))
c = float(input("Digite o terceiro lado do triângulo: "))

print("Entradas:", a, ",", b, ",", c)

if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print("Tipo de triângulo: equilátero")
    elif a == b or b == c or a == c:
        print("Tipo de triângulo: isósceles")
    else:
        print("Tipo de triângulo: escaleno")
else:
    print("Tipo de triângulo: inválido")
