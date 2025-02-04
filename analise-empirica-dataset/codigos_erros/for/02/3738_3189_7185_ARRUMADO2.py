import numpy as np

# Inputs
medias = np.array(eval(input("Digite as médias finais dos alunos: ")))
frequencias = np.array(eval(input("Digite as frequências dos alunos: ")))
carga_horaria = int(input("Digite a carga horária da disciplina: "))

# Vetor de contagem
contagem = np.zeros(3, dtype=int)

# Loop para verificar as condições
for i in range(len(medias)):
    if frequencias[i] < (carga_horaria * 0.75):
        contagem[2] += 1  # Aluno reprovado por frequência
    elif medias[i] < 5.0:
        contagem[1] += 1  # Aluno reprovado por nota
    else:
        contagem[0] += 1  # Aluno aprovado

# Imprimir resultados
print("Número de alunos aprovados:", contagem[0])
print("Número de alunos reprovados por nota:", contagem[1])
print("Número de alunos reprovados por frequência:", contagem[2])
