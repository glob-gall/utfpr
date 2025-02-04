def calcular_H(n):
    soma = 0
    sinal = 1

    for i in range(1, n+1):
        soma += sinal / i
        sinal *= -1

    return soma

# Solicita o número de termos ao usuário
n = int(input("Digite o número de termos da série: "))

# Calcula o valor de H
resultado = calcular_H(n)

# Imprime o resultado
print("H =", "{:.6f}".format(resultado))
