# Cat API Anime


```
anime$ uv run fastapi dev app/main.py --host 0.0.0.0 --port 4000

anime$ uv run pytest -v

docker compose up --build

docker compose exec anime uv run pytest -v

```


{ 
    "id" : ,
    "titol": ,
    
    "episodis" : ,

}

# docker-compose

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

