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

## How to build the docker image
```
# To start the app and redis
docker-compose up --build

# And to remove
docker image rm -f finadvisor-fin-advisor
```

#### Report com a análise da ação.

![JBSS3](images/advisor_report.jpeg)

![DASH](images/online_dashboard.png)

#### Report com o detalhamento da carteira.

- To-Do - WIP

## Referencias <a name = "referencies"></a>

- Telegram Bot: https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id
