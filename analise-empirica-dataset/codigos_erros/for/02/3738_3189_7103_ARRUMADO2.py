import numpy as np

medias = np.array(eval(input("Digite as médias finais dos alunos: ")))
presenca = np.array(eval(input("Digite as presenças dos alunos: ")))
carga_horaria = int(input("Digite a carga horária da disciplina: "))

vet = np.zeros(3, dtype=int)

for i in range(len(medias)):
    if medias[i] >= 5.0 and presenca[i] >= 0.75 * carga_horaria:
        vet[0] += 1
    elif medias[i] < 5.0 and presenca[i] >= 0.75 * carga_horaria:
        vet[1] += 1
    elif presenca[i] < 0.75 * carga_horaria:
        vet[2] += 1

print("Número de alunos aprovados:", vet[0])
print("Número de alunos reprovados por nota:", vet[1])
print("Número de alunos reprovados por frequência:", vet[2])
