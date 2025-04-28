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
            page_number = 1  # Inicia na página 1
            max_pages = 100  # Número máximo de páginas a capturar

            # Função para interceptar respostas
            async def handle_response(response):
                try:
                    if "raichu-io-site-search-v1" in response.url:
                        print(f"Capturando resposta da URL: {response.url}")

                        # Captura a resposta JSON
                        body = await response.json()
                        complainResult = body.get("complainResult", {})
                        complains = complainResult.get("complains", {})
                        data = complains.get("data", [])

                        # Salvar a resposta em um arquivo JSON
                        file_name = f"./scrap/response_page_{page_number}.json"
                        with open(file_name, "w", encoding="utf-8") as file:
                            json.dump(data, file, indent=4, ensure_ascii=False)

                        print(f"Resposta salva em {file_name}")

                except Exception as e:
                    print(f"Erro ao processar a resposta: {e}")

            # Adicionar evento para capturar respostas
            page.on("response", handle_response)

            # Acessa a página inicial
            print("Acessando a página inicial...")
            await page.goto("https://www.reclameaqui.com.br/busca/?q=Piauí")

            # Aguarda que o elemento da tabela seja carregado
            print("Aguardando o carregamento completo da página...")
            await page.wait_for_timeout(5000)

            # Loop para acessar diferentes páginas
            while page_number <= max_pages:
                print(f"Acessando a página {page_number}...")

                # Espera um pouco para capturar as requisições da página atual
                await page.wait_for_timeout(8000)

                # Salva os dados da página atual
                print(f"Dados da página {page_number} capturados.")

                # Tenta clicar no botão "Próxima página"
                try:
                    next_button = await page.query_selector(
                        "//a[contains(@class, 'ng-binding') and text()='>']"
                    )
                    if next_button:
                        await next_button.click()
                        print(
                            f"Clicando no botão para a próxima página ({page_number + 1})..."
                        )
                        page_number += 1
                    else:
                        print("Botão de próxima página não encontrado. Finalizando...")
                        break
                except Exception as e:
                    print(f"Erro ao clicar no botão de próxima página: {e}")
                    break

            await browser.close()
            print("Navegador fechado.")
        except Exception as e:
            print(f"Erro durante a execução: {e}")


asyncio.run(main())
