# FinAdvisor

## Índice

- [Sobre](#about)
- [Funcionalidades](#features)
- [Como funciona?](#how_it_works)
- [Referencias](#referencies)

## Sobre <a name = "about"></a>

This project was created in 2021 when I was thinking about automating my stock market analysis to know if there was a buy or sell momentum, that bot gathers the historical prices for almost all companies listed in the Brazilan Stock Market, applies the MACD analysis and show only stocks in an interesting momentum to buy or sell, with this automation we can analyse all stocks in a minute instead of 2+ hours.

## Funcionalidades <a name = "features"></a>

- [ ]  Strategies
    - [ ]  Macdh
        - [X]  Macdh (Semanal)
        - [ ]  Macdh (Diário)
    - [ ]  RSI
    - [ ]  Momentum
    - [ ] PEG Ratio Ranking

- [ ]  Reports
    - [X]  Enviar reports via Telegram.
    - [ ]  Report detalhado da carteira.

- [ ]  Dashboards Online
     - [ ]  Detalhamento de carteira.

- [ ]  Infra
    - [X]  Cache com redis.
    - [ ]  Banco de dados (Persistir os dados da carteira)
    - [X]  Dashboard online - Streamlite.

- [ ]  Python
    - [X]  Requirements
    - [ ]  Virtual Env
    - [X]  Dockerfile


## Como funciona? <a name = "how_it_works"></a>

Até o momento o bot analisa todas as ações da B3 e envia pelo telegram os reports de cada ação que ele encontrou um possível ponto de compra nos últimos 4 períodos.

#### Report com a análise da ação.

![JBSS3](images/advisor_report.jpeg)

![DASH](images/online_dashboard.png)

#### Report com o detalhamento da carteira.

- To-Do - WIP

## Referencias <a name = "referencies"></a>

- Telegram Bot: https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id
