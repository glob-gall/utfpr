produtos = ["ARROZ", "FEIJAO", "BIS", "MIOJO", "FANTA"]
custos = [1.25, 2.60, 1.80, 0.85, 3.20]

vn = input("Digite os produtos comprados (separados por vírgula): ").split(",")
vq = list(map(int, input("Digite as quantidades correspondentes (separadas por vírgula): ").split(",")))

total = 0

for i in range(len(vn)):
    produto = vn[i]
    quantidade = vq[i]
    indice = produtos.index(produto)
    custo = custos[indice]
    total += custo * quantidade

print("Total da conta: R$", format(total, ".2f"))
