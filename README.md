# QAdvisor

## Índice

- [Sobre](#about)
- [Funcionalidades](#features)
- [Como funciona?](#how_it_works)
- [Referencias](#referencies)

## Sobre <a name = "about"></a>

Bot escrito para ajudar na escolha de investimentos e gerenciamento de carteira.

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
    - [ ]  Flask no GCP (Cloud Run) com terraform.
    - [ ]  Banco de dados (Persistir os dados da carteira)
    - [ ]  Dashboard online.

- [ ]  Python
    - [ ]  Requirements
    - [ ]  Virtual Env
    - [ ]  Dockerfile


## Como funciona? <a name = "how_it_works"></a>

Até o momento o bot analisa todas as ações da B3 e envia pelo telegram os reports de cada ação que ele encontrou um possível ponto de compra nos últimos 4 períodos.

#### Report com a análise da ação.

![JBSS3](images/advisor_report.jpeg)

#### Report com o detalhamento da carteira.

- To-Do - WIP

## Referencias <a name = "referencies"></a>

- Telegram Bot: https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id