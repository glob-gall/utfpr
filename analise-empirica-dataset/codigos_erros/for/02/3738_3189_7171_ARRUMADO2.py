mf = eval(input("Digite as médias finais dos alunos: "))
fq = eval(input("Digite as frequências dos alunos: "))
ch = float(input("Digite a carga horária da disciplina: "))

vet = [0, 0, 0]  # [aprovados, reprovados por nota, reprovados por frequência]
fqmin = ch * 0.75

for i in range(len(mf)):
    if mf[i] >= 5 and fq[i] >= fqmin:
        vet[0] += 1
    elif mf[i] < 5:
        vet[1] += 1
    elif fq[i] < fqmin:
        vet[2] += 1

print(vet)
