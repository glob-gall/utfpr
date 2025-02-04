notas = eval(input("Digite as médias finais dos alunos: "))
frequencias = eval(input("Digite as frequências dos alunos: "))
carga_horaria = int(input("Digite a carga horária da disciplina: "))

aprovados = 0
reprovados_nota = 0
reprovados_frequencia = 0

for i in range(len(notas)):
    media = notas[i]
    frequencia = frequencias[i]

    if media >= 5.0 and frequencia >= (0.75 * carga_horaria):
        aprovados += 1
    elif media < 5.0 and frequencia >= (0.75 * carga_horaria):
        reprovados_nota += 1
    else:
        reprovados_frequencia += 1

resultado = [aprovados, reprovados_nota, reprovados_frequencia]
print(resultado)
