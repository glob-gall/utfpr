import numpy as np

medias = np.array(eval(input("Digite as médias finais dos alunos: ")))
pres = np.array(eval(input("Digite a presença (número de horas) dos alunos: ")))
ch = int(input("Digite a carga horária da disciplina: "))
ap = 0
repf = 0
repn = 0

for i in range(len(medias)):
    if pres[i] < 0.75 * ch:
        repf += 1
    elif medias[i] < 5.0:
        repn += 1
    else:
        ap += 1

resultados = np.array([ap, repn, repf])
print("Número de alunos aprovados, reprovados por nota e reprovados por frequência:", resultados)
