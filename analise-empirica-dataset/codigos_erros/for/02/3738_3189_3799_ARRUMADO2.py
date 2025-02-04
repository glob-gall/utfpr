import numpy as np

notas = np.array(eval(input("Digite as médias finais dos alunos: ")))
frequencias = np.array(eval(input("Digite as frequências dos alunos: ")))
carga_horaria = int(input("Digite a carga horária da disciplina: "))

aprovados = 0
reprovados_nota = 0
reprovados_frequencia = 0

for i in range(len(notas)):
    if notas[i] >= 5.0 and frequencias[i] >= 0.75 * carga_horaria:
        aprovados += 1
    elif notas[i] < 5.0 and frequencias[i] >= 0.75 * carga_horaria:
        reprovados_nota += 1
    else:
        reprovados_frequencia += 1

resultado = np.array([aprovados, reprovados_nota, reprovados_frequencia])
print(resultado)
