def verificar_aprovacao(notas, frequencias, carga_horaria):
    aprovados = 0
    reprovados_nota = 0
    reprovados_frequencia = 0

    for nota, frequencia in zip(notas, frequencias):
        media_minima = 5.0
        frequencia_minima = carga_horaria * 0.75

        if frequencia < frequencia_minima:
            reprovados_frequencia += 1
        elif nota < media_minima:
            reprovados_nota += 1
        else:
            aprovados += 1

    return [aprovados, reprovados_nota, reprovados_frequencia]

# Exemplo de utilização:
medias = [7.5, 4.0, 9.0, 6.5, 8.0]
frequencias = [40, 35, 50, 45, 48]
carga_horaria = 60

resultado = verificar_aprovacao(medias, frequencias, carga_horaria)
print("Alunos aprovados:", resultado[0])
print("Alunos reprovados por nota:", resultado[1])
print("Alunos reprovados por frequência:", resultado[2])
