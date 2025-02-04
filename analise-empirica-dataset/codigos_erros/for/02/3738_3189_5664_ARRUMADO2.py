import numpy as np

medias = np.array(eval(input("Digite as médias finais dos alunos: ")))
presenca = np.array(eval(input("Digite as presenças dos alunos: ")))
carga_horaria = int(input("Digite a carga horária da disciplina: "))

contagem = np.zeros(3, dtype=int)
frequencia_minima = carga_horaria * 0.75

for i in range(np.size(medias)):
    if medias[i] >= 5.0 and presenca[i] >= frequencia_minima:
        contagem[0] += 1
    elif medias[i] < 5.0 and presenca[i] >= frequencia_minima:
        contagem[1] += 1
    elif presenca[i] < frequencia_minima:
        contagem[2] += 1

print("Número de alunos aprovados:", contagem[0])
print("Número de alunos reprovados por nota:", contagem[1])
print("Número de alunos reprovados por frequência:", contagem[2])
