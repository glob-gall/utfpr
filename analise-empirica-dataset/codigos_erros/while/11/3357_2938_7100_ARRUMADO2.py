import math

# Entrada de dados
a = float(input("Distância entre o observador e a primeira árvore: "))
b = float(input("Distância entre o observador e a segunda árvore: "))
gamma = float(input("Ângulo entre a e b (em graus): "))

# Conversão de graus para radianos
gamma_rad = math.radians(gamma)

# Cálculo da distância entre as duas árvores
c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(gamma_rad))

# Saída do resultado arredondado para duas casas decimais
print("Distância entre as duas árvores:", round(c, 2))
