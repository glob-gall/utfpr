maisVotado = int(input("Informe o numero de votos do candidato mais votado: "))
segundo = int(input("Informe o numero de votos do candidato em segundo lugar: "))
menosVotado = int(input("Informe o numero de votos do candidao menos votado: ")) 

if(maisVotado >= segundo*2):
	print("NAO")
else:
	print("SIM")