import csv
import requests

# Cabeçalhos do CSV
CSV_HEADERS = ["Título", "Empresa", "Data Criação", "Status", "Link"]

# Configurações
TERMO_BUSCA = "Teresina"
ITENS_POR_PAGINA = 10


def main():
    all_reclamacoes = []
    pagina = 1

    while True:
        print(f"Abrindo página {pagina}...")

        # URL da API
        api_url = f"https://iosearch.reclameaqui.com.br/raichu-io-site-search-v1/query/{TERMO_BUSCA}/{ITENS_POR_PAGINA}/{pagina}"

        # Headers da requisição
        headers = {
            ":authority": "iosearch.reclameaqui.com.br",
            ":method": "GET",
            ":scheme": "https",
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9",
            "origin": "https://www.reclameaqui.com.br",
            "referer": "https://www.reclameaqui.com.br/",
            "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Opera";v="117"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 OPR/117.0.0.0",
        }

        # Fazer a requisição à API
        response = requests.get(api_url, headers=headers)

        if response.status_code != 200:
            print(f"Erro na requisição à API: {response.status_code}")
            break

        data = response.json()
        hits = data.get("hits", [])
        if not hits:
            print("Nenhum resultado encontrado, terminando.")
            break

        for item in hits:
            titulo = item.get("title", "")
            empresa = item.get("company", {}).get("name", "")
            data_criacao = item.get("createdAt", "")
            status = item.get("status", "")
            link = f"https://www.reclameaqui.com.br{item.get('url', '')}"

            all_reclamacoes.append(
                {
                    "Título": titulo,
                    "Empresa": empresa,
                    "Data Criação": data_criacao,
                    "Status": status,
                    "Link": link,
                }
            )

        pagina += 1

    # Salvando no CSV
    with open("reclamacoes.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_HEADERS)
        writer.writeheader()
        for rec in all_reclamacoes:
            writer.writerow(rec)

    print("Scraping finalizado! Dados salvos em reclamacoes.csv")


if __name__ == "__main__":
    main()
