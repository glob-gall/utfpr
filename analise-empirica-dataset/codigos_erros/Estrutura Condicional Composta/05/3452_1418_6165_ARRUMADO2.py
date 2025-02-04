maisVotado = int(input("Informe o número de votos do candidato mais votado: "))
segundo = int(input("Informe o número de votos do candidato em segundo lugar: "))
menosVotado = int(input("Informe o número de votos do candidato menos votado: "))

if maisVotado > (segundo + menosVotado):
    print("NAO")
else:
    print("SIM")
