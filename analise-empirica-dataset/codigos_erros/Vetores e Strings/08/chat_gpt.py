def data_por_extenso(data):
    dia = data[0:2]
    mes = data[2:4]
    ano = data[4:]

    # Dicionários com os meses e seus respectivos nomes por extenso
    meses = {
        "01": "janeiro",
        "02": "fevereiro",
        "03": "marco",
        "04": "abril",
        "05": "maio",
        "06": "junho",
        "07": "julho",
        "08": "agosto",
        "09": "setembro",
        "10": "outubro",
        "11": "novembro",
        "12": "dezembro"
    }

    # Imprime a data por extenso
    print(f"{dia} de {meses[mes]} de {ano}")


# Exemplo de uso
data = input("Digite a data no formato ddmmaaaa: ")
data_por_extenso(data)
