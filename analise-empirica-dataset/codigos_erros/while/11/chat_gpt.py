import math

a = float(input("Distância entre o observador e a primeira árvore: "))
b = float(input("Distância entre o observador e a segunda árvore: "))
angulo = float(input("Ângulo entre a e b (em graus): "))

# Converter o ângulo de graus para radianos
angulo_rad = math.radians(angulo)

# Calcular a distância c usando a fórmula do cosseno
c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(angulo_rad))

# Arredondar a distância para duas casas decimais
c_arredondado = round(c, 2)

# Saída
print(c_arredondado)
