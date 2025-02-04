# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input("lado 1: "))
b = float(input("lado 2: "))
c = float(input("lado 3: "))

print("Entradas:", a, ",", b, ",", c)

if a > 0 and b > 0 and c > 0:
    if a < b + c and b < a + c and c < a + b:
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
