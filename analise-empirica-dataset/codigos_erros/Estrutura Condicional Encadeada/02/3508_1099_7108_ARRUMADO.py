a = float(input())
b = float(input())
c = float(input())

if a > 0 and b > 0 and c > 0:
    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            print("Entradas:", a, b, c)
            print("Tipo de triângulo: equilátero")
        elif a == b or a == c or b == c:
            print("Entradas:", a, ",", b, ",", c)
            print("Tipo de triângulo: isósceles")
        else:
            print("Entradas:", a, ",", b, ",", c)
            print("Tipo de triângulo: escaleno")
    else:
        print("Entradas:", a, ",", b, ",", c)
        print("Tipo de triângulo: inválido")
else:
    print("Entradas:", a, ",", b, ",", c)
    print("Tipo de triângulo: inválido")
