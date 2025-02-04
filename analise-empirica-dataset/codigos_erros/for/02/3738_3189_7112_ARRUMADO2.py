import numpy as np

medias = np.array(eval(input("Digite as médias finais dos alunos: ")))
frequencias = np.array(eval(input("Digite as frequências dos alunos: ")))
carga_horaria = int(input("Digite a carga horária da disciplina: "))

limite_frequencia = 0.75 * carga_horaria

num_aprovados = np.sum((medias >= 5.0) & (frequencias >= limite_frequencia))
num_reprovados_nota = np.sum((medias < 5.0) & (frequencias >= limite_frequencia))
num_reprovados_frequencia = np.sum(frequencias < limite_frequencia)

resultado = np.array([num_aprovados, num_reprovados_nota, num_reprovados_frequencia])

print("Resultado:")
print(resultado)
