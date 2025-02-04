produtos = {
    "ARROZ": 1.25,
    "FEIJAO": 2.60,
    "BIS": 1.80,
    "MIOJO": 0.85,
    "FANTA": 3.20
}

nomes = input("Digite os nomes dos produtos (separados por vírgula): ").split(",")
quantidades = input("Digite as quantidades dos produtos (separadas por vírgula): ").split(",")

total = 0

for i in range(len(nomes)):
    produto = nomes[i]
    quantidade = int(quantidades[i])
    
    if produto in produtos:
        custo = produtos[produto]
        total += custo * quantidade

print(f"Total da conta: R$ {total:.2f}")
