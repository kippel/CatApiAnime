# Cat API Anime

## FastAPI

```
anime$ uv run fastapi dev app/main.py --host 0.0.0.0 --port 4000

anime$ uv run pytest -v
```

---

## Docker

```
docker compose up --build
docker compose -f docker-compose.dev.yml up --build


docker compose exec anime uv run python -m app.cli

docker compose exec anime uv run pytest -v
```

## docker-compose

```
services:
  anime:
    build: ./anime
    ports:
      - "4000:4000"
    volumes:
      - ./anime/sql_app_test.db:/app/sql_app_test.db
    environment:
      - DATABASE_URL=sqlite:///sql_app_test.db
```

---

# Anime

```
{
  "titol": "Bola de drac",
  "sinopsi": "",
  "primer_episodi": "26-02-1986",
  "film": "MANGA",
  "tipus": "SERIE",
}
```


# AnimeSeries

```
{
  "durada_dels_capiols" : "25 min",
  "ultim_episodi : "20 abril 1976",
  "temporades" : 2,
  "episodis : 104,
}
```





