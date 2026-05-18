# leddit-scrap

Scraper de subreddits do Reddit **sem API key** — usa o feed JSON público do Reddit.

## Funcionalidades

- Busca posts por ordenação: `hot`, `new`, `top`, `rising`
- Coleta comentários com respostas aninhadas
- Saída em JSON (stdout ou arquivo)
- Rate-limit respeitado via delay configurável

## Instalação

```bash
pip install -r requirements.txt
```

## Uso

```bash
# Listar os 10 posts mais quentes de r/dataengineering
python main.py dataengineering

# Top 25 posts + comentários, salvar em arquivo
python main.py dataengineering --sort top --limit 25 --comments --output resultado.json

# Novos posts de r/python
python main.py python --sort new --limit 20
```

## Opções

| Opção | Padrão | Descrição |
|---|---|---|
| `subreddit` | — | Nome do subreddit (sem `r/`) |
| `--sort` | `hot` | Ordenação: `hot`, `new`, `top`, `rising` |
| `--limit` | `10` | Número de posts (1–100) |
| `--comments` | desativado | Busca comentários de cada post |
| `--output` | stdout | Arquivo `.json` de saída |

## Uso como biblioteca

```python
from scraper.reddit import RedditScraper

scraper = RedditScraper(delay=1.0)

# Posts
posts = scraper.get_posts("dataengineering", sort="hot", limit=5)

# Comentários de um post específico
comments = scraper.get_comments("dataengineering", post_id="abc123")
```

## Estrutura

```text
leddit-scrap/
├── main.py              # CLI
├── requirements.txt
├── README.md
└── scraper/
    ├── __init__.py
    └── reddit.py        # RedditScraper
```

## Notas

- Usa o endpoint público `reddit.com/r/{sub}/{sort}.json` — sem OAuth
- Respeite os [Termos de Uso do Reddit](https://www.redditinc.com/policies/user-agreement)
- User-Agent identificado conforme boas práticas da plataforma