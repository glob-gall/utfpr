votos_candidato1 = int(input("Digite o número de votos do candidato mais votado: "))
votos_candidato2 = int(input("Digite o número de votos do candidato em segundo lugar: "))
votos_candidato3 = int(input("Digite o número de votos do candidato menos votado: "))

total_votos_validos = votos_candidato1 + votos_candidato2 + votos_candidato3

if votos_candidato1 > total_votos_validos / 2 and total_votos_validos > 200000:
    print("NAO")
else:
    print("SIM")
