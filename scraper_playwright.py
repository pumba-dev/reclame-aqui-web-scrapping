import asyncio
import json
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(
                headless=False  # headless=False para abrir a janela do navegador
            )
            context = await browser.new_context()
            page = await context.new_page()

            # Variáveis para controle do loop
            base_url = "https://iosearch.reclameaqui.com.br/raichu-io-site-search-v1/query/Teresina/10/"
            page_number = 0  # Inicia na página 0
            max_pages = 10  # Número máximo de páginas a capturar

            # Função para interceptar respostas
            async def handle_response(response):
                try:
                    if base_url in response.url:
                        print(f"Capturando resposta da URL: {response.url}")
                        body = await response.json()

                        # Salvar a resposta em um arquivo JSON
                        file_name = f"./scrap/response_page_{page_number}.json"
                        with open(file_name, "w", encoding="utf-8") as file:
                            json.dump(body, file, indent=4, ensure_ascii=False)
                        print(f"Resposta salva em {file_name}")
                except Exception as e:
                    print(f"Erro ao processar a resposta: {e}")

            # Adicionar evento para capturar respostas
            page.on("response", handle_response)

            # Loop para acessar diferentes páginas
            while page_number < max_pages:
                print(f"Acessando a página {page_number}...")

                await page.goto(f"{base_url}{page_number}")

                await page.wait_for_timeout(
                    5000
                )  # Espera 5 segundos para capturar a resposta

                page_number += 10  # Incrementa em 10

            await browser.close()
            print("Navegador fechado.")
        except Exception as e:
            print(f"Erro durante a execução: {e}")


asyncio.run(main())
