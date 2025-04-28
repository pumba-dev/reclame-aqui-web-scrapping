import os
import json
import csv

# Caminho da pasta contendo os arquivos JSON
folder_path = "scrap"

# Nome do arquivo CSV de saída
output_csv = "reclamacoes_completas3.csv"

# Lista para armazenar todas as reclamações
all_reclamacoes = []

# Iterar sobre todos os arquivos na pasta
for file_name in os.listdir(folder_path):
    if file_name.endswith(".json"):
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                # Adicionar cada item do JSON à lista
                for item in data:
                    all_reclamacoes.append(item)
            except json.JSONDecodeError as e:
                print(f"Erro ao processar {file_name}: {e}")

# Obter todos os campos únicos presentes nos itens
all_fields = set()
for reclamacao in all_reclamacoes:
    all_fields.update(reclamacao.keys())

# Converter o conjunto de campos para uma lista ordenada
all_fields = sorted(all_fields)

# Escrever os dados no arquivo CSV
with open(output_csv, mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=all_fields)
    writer.writeheader()
    for reclamacao in all_reclamacoes:
        writer.writerow(reclamacao)

print(f"Base CSV criada com sucesso: {output_csv}")
