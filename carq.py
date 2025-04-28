import os

# Caminho da pasta onde os arquivos serão criados
folder_path = "pages"

# Certifique-se de que a pasta existe
os.makedirs(folder_path, exist_ok=True)

# Criar arquivos JSON de 1 a 100
for i in range(1, 101):
    file_name = f"{i:02}.json"  # Nome do arquivo (ex: 01.json, 02.json, ...)
    file_path = os.path.join(folder_path, file_name)

    # Verificar se o arquivo já existe
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            pass  # Cria um arquivo vazio
        print(f"Arquivo criado: {file_name}")
    else:
        print(f"Arquivo já existe: {file_name}")
