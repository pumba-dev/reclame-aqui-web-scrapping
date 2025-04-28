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

            # Escutar todas as respostas
            async def handle_response(response):
                try:
                    if "raichu-io-site-search-v1" in response.url:
                        print(f"Capturando resposta da URL: {response.url}")
                        body = await response.json()
                        complainResult = body["complainResult"]
                        complains = complainResult["complains"]
                        data = complains["data"]

                        # Salvar a resposta em um arquivo JSON
                        with open("response.json", "w", encoding="utf-8") as file:
                            json.dump(data, file, indent=4, ensure_ascii=False)
                        print("Resposta salva em response.json")
                except Exception as e:
                    print(f"Erro ao processar a resposta: {e}")

            # Adicionar eventos para capturar requisições e respostas

            page.on("response", handle_response)

            # Acessa a página
            print("Acessando a página...")
            await page.goto("https://www.reclameaqui.com.br/busca/?q=Teresina")

            # Aguarda que um elemento específico da página seja carregado
            print("Aguardando o carregamento completo da página...")
            await page.wait_for_selector(
                "div[data-testid='search-results']", timeout=15000
            )

            # Espera um pouco para capturar todas as requisições e respostas
            print("Esperando as requisições serem capturadas...")
            await page.wait_for_timeout(5000)  # Espera 5 segundos adicionais

            await browser.close()
            print("Navegador fechado.")
        except Exception as e:
            print(f"Erro durante a execução: {e}")


asyncio.run(main())
