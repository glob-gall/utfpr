import unittest
import sys
import io
from math import pi


def verificar_string(string1, valores_entrada,arquivo):
    # Abre o arquivo 'codigo.py' e lê o seu conteúdo
    with open(arquivo, 'r') as file:
        codigo = file.read()

    # Redireciona a saída padrão para um objeto io.StringIO
    stdout_backup = sys.stdout
    sys.stdout = io.StringIO()

    # Cria um iterador para fornecer os valores de entrada sequencialmente
    input_mock = iter(valores_entrada)

    # Função de input mockada para retornar os valores do iterador
    def input_mock_function(*args):
        return next(input_mock)

    try:
        # Executa o código lido do arquivo com o input mockado
        exec(codigo, {'input': input_mock_function})
        valor_impresso1 = sys.stdout.getvalue().strip()

    except Exception as e:
        print(f"Erro ao executar o código: {e}")
        return False
    finally:
        # Restaura a saída padrão
        sys.stdout = stdout_backup

    # Verifica se os valores impressos são iguais às strings fornecidas
    return string1 == valor_impresso1


class TestStringVerification(unittest.TestCase):
    file = 'codigo.py'
    
    def test_verificar_string_1(self):
        valores_entrada = ["12.5", "17.2", "64.9"]
        self.assertTrue(verificar_string("16.42", valores_entrada,self.file))

    def test_verificar_string_2(self):
        valores_entrada = ["2.33", "4.09", "12.3"]
        self.assertTrue(verificar_string("1.88", valores_entrada,self.file))

    def test_verificar_string_3(self):
        valores_entrada = ["55.0", "3.0", "77.6"]
        self.assertTrue(verificar_string("54.43", valores_entrada,self.file))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        TestStringVerification.file = sys.argv.pop()
    unittest.main()
