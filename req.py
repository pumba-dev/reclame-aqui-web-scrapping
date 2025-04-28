import httpx
import json

# URL da API
url = (
    "https://iosearch.reclameaqui.com.br/raichu-io-site-search-v1/query/Teresina/10/10"
)

# Headers da requisição
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "if-modified-since": "Sun, 27 Apr 2025 18:36:02 GMT",
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

# Cookies necessários
cookies = {
    "__cf_bm": "tatO34tQf3tycsyD0Xf9ybCQNewRjFI3o7hZIO77b_E",
    "_cfuvid": "bg7JhJ9qxFyA_AJECYZbcaPimKw1BEQKLLgao8ebls8",
}

# Fazer a requisição com httpx
with httpx.Client(headers=headers, cookies=cookies) as client:
    response = client.get(url)

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4, ensure_ascii=False))
    else:
        print(f"Erro na requisição: {response.status_code}")
