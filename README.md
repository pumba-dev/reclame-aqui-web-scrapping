# Reclame Aqui Web Scraping

Este projeto realiza o web scraping das últimas reclamações registradas no site **Reclame Aqui**, utilizando a biblioteca **Playwright**. O objetivo é capturar os dados das reclamações e salvá-los em arquivos JSON para posterior processamento e análise.

## Como funciona o código

1. **Navegação automatizada**:

   - O script utiliza o **Playwright** para abrir o navegador e acessar a página de busca do Reclame Aqui.
   - Ele navega por múltiplas páginas de resultados, capturando as informações das reclamações.

2. **Interceptação de respostas**:

   - O código intercepta as respostas HTTP que contêm os dados das reclamações no formato JSON.
   - Essas informações são extraídas e salvas em arquivos JSON na pasta scrap.

3. **Controle de navegação**:

   - O script percorre até 100 páginas de resultados (ou menos, caso não haja mais páginas disponíveis).
   - Ele tenta clicar no botão "Próxima página" para continuar a captura.

4. **Armazenamento dos dados**:
   - Cada página de reclamações é salva em um arquivo JSON separado, nomeado como `response_page_<número_da_página>.json`.

## Estrutura dos dados capturados

As reclamações capturadas possuem as seguintes colunas:

- **id**: Identificador único da reclamação no Reclame Aqui.
- **company_name**: Nome da empresa contra a qual a reclamação foi registrada.
- **category**: Código numérico que indica a categoria geral da reclamação. Exemplos:
  - `0`: Não encontrei meu problema
  - `3`: Cartões de Crédito
  - `16`: Ônibus Rodoviário
  - `18`: Companhias Aéreas
  - `33`: Planos de Saúde
  - `43`: Salões e Centros de Estética
  - `55`: Bolsas e Malas
  - `118`: Logística e Entrega Rápida
  - `233`: Moda Feminina
  - `255`: Problemas com o Atendimento
  - `260`: Problemas na Loja
- **title**: Título da reclamação.
- **description**: Texto completo do relato do consumidor.
- **created_at**: Data e hora em que a reclamação foi postada.
- **first_interaction_at**: Data e hora da primeira interação subsequente.
- **updated_at**: Data e hora da última atualização na reclamação.
- **status**: Estado atual da reclamação (ex.: `PENDING`, `IN_PROGRESS`, `SOLVED`).
- **score**: Nota atribuída pelo consumidor ao atendimento recebido.
- **evaluation**: Avaliação pós-atendimento deixada pelo consumidor.
- **deal_again**: Indica se o consumidor negociaria novamente com a empresa (`True` ou `False`).
- **has_reply**: Indica se a empresa respondeu à reclamação (`True` ou `False`).
- **solved**: Indica se a reclamação foi solucionada (`True` ou `False`).
- **user_city**: Cidade de origem do reclamante.
- **user_state**: Estado de origem do reclamante.
- **resolution_time_days**: Tempo em dias entre a primeira interação e a última atualização.

## Processamento dos dados

Após a captura, os dados podem ser processados para análise. O pipeline de processamento inclui:

1. **Carregamento e inspeção inicial**:

   - O dataset original contém 100 registros e 68 colunas, mas muitas são irrelevantes.

2. **Seleção de colunas essenciais**:

   - Apenas 17 colunas são mantidas, como identificadores, informações da empresa, texto da reclamação, datas-chave, status e métricas de avaliação.

3. **Padronização de nomes**:

   - Colunas são renomeadas para o formato `snake_case` (ex.: `created` → `created_at`).

4. **Conversão de datas**:

   - Datas são convertidas para o formato `datetime`.

5. **Criação de nova variável**:

   - `resolution_time_days`: Diferença em dias entre a primeira interação e a última atualização.

6. **Limpeza de texto**:

   - Títulos e descrições são convertidos para minúsculas e espaços desnecessários são removidos.

7. **Tratamento de valores ausentes**:

   - Valores nulos são substituídos por `'Desconhecido'`.

8. **Reordenação das colunas**:
   - As colunas são organizadas de forma lógica para facilitar a análise.

## Requisitos

- Python 3.8 ou superior
- Bibliotecas necessárias:
  - `playwright`
  - `asyncio`
  - `json`

## Como executar

1. **Instale as dependências**:

   ```bash
   pip install playwright
   playwright install
   ```

2. **Execute o script**:

   ```bash
   python sc_playwright.py
   ```

3. **Verifique os arquivos JSON**:
   - Os arquivos serão salvos na pasta scrap.

## Observações

- Certifique-se de que a pasta scrap existe antes de executar o script.
- O navegador será aberto em modo não-headless para facilitar o monitoramento do processo.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades para o projeto.
