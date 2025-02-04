produtos = ["ARROZ", "FEIJAO", "BIS", "MIOJO", "FANTA"]
custos = [1.25, 2.60, 1.80, 0.85, 3.20]

nomes_produtos = input("Informe os produtos comprados (separados por vírgula): ")
quantidades_str = input("Informe as quantidades dos produtos (separadas por vírgula): ")

nomes = nomes_produtos.split(",")
quantidades = list(map(float, quantidades_str.split(",")))

total = 0

for i in range(len(nomes)):
    nome = nomes[i]
    quantidade = quantidades[i]

    if nome in produtos:
        indice = produtos.index(nome)
        custo = custos[indice]
        total += custo * quantidade

total = round(total, 2)

print("Total da conta: R$", total)
