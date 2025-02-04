import os
import shutil

diretorio_pai = "/home/viniciuspetris/Downloads/Mestrado/Empirica/codigos"
numero = "3056"
diretorio_destino = "/home/viniciuspetris/Downloads/teste/09"

# Verificar se o diretório de destino existe, se não, criá-lo
if not os.path.exists(diretorio_destino):
    os.makedirs(diretorio_destino)

# Percorrer todas as pastas dentro do diretório pai
for nome_pasta in os.listdir(diretorio_pai):
    diretorio_pasta = os.path.join(diretorio_pai, nome_pasta)

    if os.path.isdir(diretorio_pasta):
        diretorio_codes = os.path.join(diretorio_pasta, "codes")

        if os.path.exists(diretorio_codes):
            # Obter o número da pasta pai
            numero_pasta_pai = nome_pasta

            # Copiar os arquivos com o número "1015" no nome para o diretório de destino
            for nome_arquivo in os.listdir(diretorio_codes):
                if numero in nome_arquivo:
                    nome_arquivo_original, extensao = os.path.splitext(nome_arquivo)
                    caminho_origem = os.path.join(diretorio_codes, nome_arquivo)
                    caminho_destino = os.path.join(diretorio_destino, f"{nome_arquivo_original}_{numero_pasta_pai}{extensao}")
                    shutil.copy2(caminho_origem, caminho_destino)
                    print(f"Copiado: {caminho_origem} -> {caminho_destino}")

