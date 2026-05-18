# leddit-scrap

Scraper de subreddits do Reddit sem API key, usando o feed JSON publico da plataforma.

## Funcionalidades

- Busca posts por ordenacao: `hot`, `new`, `top`, `rising`
- Estrutura organizada para coleta, persistencia, utilitarios, scripts e testes
- Saida em JSON com ponto de extensao para CSV e banco de dados
- Configuracao centralizada por ambiente

## Instalacao

```bash
pip install -r requirements.txt
```

## Uso

```bash
# Listar os 10 posts mais quentes de r/dataengineering
PYTHONPATH=src python -m leddit_scrap.main dataengineering

# Salvar o resultado em JSON
PYTHONPATH=src python scripts/run_scraper.py python --sort new --limit 20 --output data/exports/python.json
```

## Estrutura

```text
leddit-scrap/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── src/
│   └── leddit_scrap/
│       ├── __init__.py
│       ├── main.py
│       ├── config.py
│       ├── scraper/
│       │   ├── __init__.py
│       │   ├── reddit_client.py
│       │   ├── collectors.py
│       │   └── parsers.py
│       ├── storage/
│       │   ├── __init__.py
│       │   ├── writer_csv.py
│       │   ├── writer_json.py
│       │   └── writer_db.py
│       └── utils/
│           ├── __init__.py
│           ├── logging.py
│           └── helpers.py
├── data/
│   ├── raw/
│   ├── processed/
│   └── exports/
├── tests/
│   ├── test_scraper.py
│   └── test_storage.py
└── scripts/
    └── run_scraper.py
```

## Notas

- O pacote principal agora fica centralizado em `src/leddit_scrap`
- A pasta `data/` foi separada em `raw`, `processed` e `exports`
- `tests/` contem a base para validacao automatizada da estrutura
- `scripts/` concentra a execucao operacional do scraper
