# leddit-scrap

Scraper de subreddits do Reddit sem API key, usando o feed JSON publico da plataforma.

## Funcionalidades

- Busca posts por ordenacao: `hot`, `new`, `top`, `rising`
- Estrutura organizada para coleta, persistencia, utilitarios, scripts e testes
- Saida em JSON com ponto de extensao para CSV e banco de dados
- Configuracao centralizada por ambiente

## Estrutura

```text
leddit-scrap/
|- README.md
|- requirements.txt
|- .env.example
|- .gitignore
|- src/
|  \- leddit_scrap/
|     |- __init__.py
|     |- main.py
|     |- config.py
|     |- scraper/
|     |  |- __init__.py
|     |  |- reddit_client.py
|     |  |- collectors.py
|     |  \- parsers.py
|     |- storage/
|     |  |- __init__.py
|     |  |- writer_csv.py
|     |  |- writer_json.py
|     |  \- writer_db.py
|     \- utils/
|        |- __init__.py
|        |- logging.py
|        \- helpers.py
|- data/
|  |- raw/
|  |- processed/
|  \- exports/
|- tests/
|  |- test_scraper.py
|  \- test_storage.py
\- scripts/
   \- run_scraper.py
```

## Runbook

### Pre-requisitos

- Python 3.10 ou superior
- Git para clonar o repositorio

```bash
git clone https://github.com/dimi1engineer/leddit-scrap.git
cd leddit-scrap
```

### Instalando dependencias

```bash
# Criar e ativar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt
```

### Configurando o ambiente

```bash
# Copiar o arquivo de exemplo
cp .env.example .env
```

Edite o `.env` conforme necessario. Variaveis disponiveis:

| Variavel | Padrao | Descricao |
|---|---|---|
| `REDDIT_BASE_URL` | `https://www.reddit.com` | Endpoint base usado para consultar o feed JSON publico |
| `REDDIT_USER_AGENT` | `leddit-scrap/0.1 (+https://github.com/dimi1engineer/leddit-scrap)` | User-Agent enviado nas requisicoes |
| `REQUEST_TIMEOUT` | `15` | Timeout das requisicoes HTTP em segundos |
| `REQUEST_DELAY` | `1.0` | Intervalo entre requisicoes |

### Executando o scraper

O scraper pode ser executado pela CLI do pacote ou pelo script operacional:

```bash
# Listar os 10 posts mais quentes de r/dataengineering
PYTHONPATH=src python -m leddit_scrap.main dataengineering

# Salvar o resultado em JSON
PYTHONPATH=src python scripts/run_scraper.py python --sort new --limit 20 --output data/exports/python.json
```

### Executando via Docker Compose

O projeto tambem pode ser executado sem dependencias locais de Python usando Docker Compose.

```bash
# Construir a imagem
docker compose build

# Listar os 10 posts mais quentes de r/dataengineering
docker compose run --rm scraper dataengineering

# Salvar o resultado em JSON no host
docker compose run --rm scraper python --sort new --limit 20 --output data/exports/python.json
```

O servico `scraper` usa:

- `python:3.12-slim` como imagem base
- `PYTHONPATH=/app/src` dentro do container
- `scripts/run_scraper.py` como entrypoint
- volume `./data:/app/data` para persistir resultados no host

Se quiser inspecionar os arquivos gerados, eles aparecerao normalmente em `data/exports/`, `data/raw/` ou `data/processed/` no repositorio local.

#### Opcoes disponiveis

| Opcao | Padrao | Descricao |
|---|---|---|
| `subreddit` | - | Nome do subreddit (sem `r/`) |
| `--sort` | `hot` | Ordenacao: `hot`, `new`, `top`, `rising` |
| `--limit` | `10` | Numero de posts requisitados |
| `--output` | stdout | Caminho opcional para salvar o JSON |

### Colhendo os resultados

Os arquivos gerados sao organizados em:

| Diretorio | Conteudo |
|---|---|
| `data/raw/` | Dados brutos coletados diretamente do Reddit |
| `data/processed/` | Dados transformados ou enriquecidos |
| `data/exports/` | Arquivos finais prontos para uso ou analise |

O formato de saida atual e JSON. A pasta `src/leddit_scrap/storage/` ja deixa preparado o caminho para expansao em CSV e banco de dados.

## Uso como biblioteca

```python
from leddit_scrap.config import get_settings
from leddit_scrap.scraper.collectors import collect_subreddit_posts

payload = collect_subreddit_posts(
    subreddit="dataengineering",
    sort="hot",
    limit=5,
    settings=get_settings(),
)
```

## Notas

- O pacote principal fica centralizado em `src/leddit_scrap`
- A pasta `data/` foi separada em `raw`, `processed` e `exports`
- `tests/` contem a base para validacao automatizada da estrutura
- `scripts/` concentra a execucao operacional do scraper
- O projeto usa o endpoint publico `reddit.com/r/{sub}/{sort}.json` sem OAuth
