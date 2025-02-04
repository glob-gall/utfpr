a = float(input())
b = float(input())
c = float(input())

print("Entradas:", a, ",", b, ",", c)

if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and c + b > a:
        if a == b and b == c:
            print("Tipo de triângulo: equilátero")
        elif a == b or b == c or a == c:
            print("Tipo de triângulo: isósceles")
        else:
            print("Tipo de triângulo: escaleno")
    else:
        print("Tipo de triângulo: inválido")
else:
    print("Tipo de triângulo: inválido")
