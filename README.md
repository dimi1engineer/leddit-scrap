# leddit-scrap

Scraper de subreddits do Reddit **sem API key** — usa o feed JSON público do Reddit.

## Funcionalidades

- Busca posts por ordenação: `hot`, `new`, `top`, `rising`
- Coleta comentários com respostas aninhadas
- Saída em JSON (stdout ou arquivo)
- Rate-limit respeitado via delay configurável

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

## Runbook

### Pré-requisitos

- Python 3.10 ou superior
- Docker instalado e em execução
- Git para clonar o repositório

```bash
git clone https://github.com/dimi1engineer/leddit-scrap.git
cd leddit-scrap
```

### Instalando dependências

```bash
# Criar e ativar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt
```

### Configurando o ambiente

```bash
# Copiar o arquivo de exemplo
cp .env.example .env
```

Edite o `.env` conforme necessário. Variáveis disponíveis:

| Variável | Padrão | Descrição |
|---|---|---|
| `DELAY` | `1.0` | Intervalo em segundos entre requisições |
| `OUTPUT_DIR` | `data/exports` | Diretório padrão de saída dos arquivos |

### Executando o scraper

O scraper é executado via CLI a partir de `scripts/run_scraper.py`:

```bash
# Listar os 10 posts mais quentes de r/dataengineering
PYTHONPATH=src python scripts/run_scraper.py dataengineering

# Top 25 posts + comentários, salvar em arquivo
PYTHONPATH=src python scripts/run_scraper.py dataengineering --sort top --limit 25 --comments --output resultado.json

# Novos posts de r/python
PYTHONPATH=src python scripts/run_scraper.py python --sort new --limit 20
```

#### Opções disponíveis

| Opção | Padrão | Descrição |
|---|---|---|
| `subreddit` | — | Nome do subreddit (sem `r/`) |
| `--sort` | `hot` | Ordenação: `hot`, `new`, `top`, `rising` |
| `--limit` | `10` | Número de posts (1–100) |
| `--comments` | desativado | Busca comentários de cada post |
| `--output` | stdout | Arquivo `.json` de saída |

### Colhendo os resultados

Os arquivos gerados são salvos em:

| Diretório | Conteúdo |
|---|---|
| `data/raw/` | Dados brutos coletados diretamente do Reddit |
| `data/processed/` | Dados após transformações e limpezas |
| `data/exports/` | Arquivos finais prontos para uso ou análise |

O formato de saída padrão é **JSON**. Para exportar em outros formatos, utilize os writers disponíveis em `src/leddit_scrap/storage/`.

## Uso como biblioteca

```python
from leddit_scrap.scraper.reddit_client import RedditScraper

scraper = RedditScraper(delay=1.0)

# Posts
posts = scraper.get_posts("dataengineering", sort="hot", limit=5)

# Comentários de um post específico
comments = scraper.get_comments("dataengineering", post_id="abc123")
```

## Notas

- Usa o endpoint público `reddit.com/r/{sub}/{sort}.json` — sem OAuth
- Respeite os [Termos de Uso do Reddit](https://www.redditinc.com/policies/user-agreement)
- User-Agent identificado conforme boas práticas da plataforma
