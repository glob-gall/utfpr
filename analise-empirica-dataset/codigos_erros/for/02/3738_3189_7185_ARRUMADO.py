import numpy as np

# Inputs
medias = np.array(eval(input("Digite as médias dos alunos: ")))
freq = np.array(eval(input("Digite as frequências dos alunos: ")))
ch = int(input("Digite a carga horária total: "))

# Vetor nominal
nom = np.zeros(3, dtype=int)

# Loop
for i in range(len(medias)):
    if freq[i] < (ch * 0.75):
        nom[2] += 1

    if medias[i] < 5.0:
        nom[1] += 1

nom[0] = len(medias) - (nom[1] + nom[2])

print("Quantidade de alunos aprovados:", nom[0])
print("Quantidade de alunos em recuperação:", nom[1])
print("Quantidade de alunos reprovados por falta:", nom[2])
