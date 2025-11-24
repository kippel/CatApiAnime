# Cat API Anime


```
anime$ uv run fastapi dev app/main.py --host 0.0.0.0 --port 4000

anime$ uv run pytest -v

docker compose up --build

docker compose exec anime uv run pytest -v

```


Gènere	manga i anime d'aventures Modifica el valor a Wikidata
Director	Hiroshi Saito Modifica el valor a Wikidata
Productor	Nippon Animation Modifica el valor a Wikidata
Companyia productora	Nippon Animation Modifica el valor a Wikidata
País	Japó Modifica el valor a Wikidata
Llengua original	japonès Modifica el valor a Wikidata
Canal original	TV Asahi Modifica el valor a Wikidata
Durada dels capítols	25 min Modifica el valor a Wikidata
Primer episodi	1r abril 1975 Modifica el valor a Wikidata
Últim episodi	20 abril 1976 Modifica el valor a Wikidata
Temporades	2 Modifica el valor a Wikidata
Episodis	104 Modifica el valor a Wikidata
Llista d'episodis	llista d'episodis de l'abella Maia

# AnimeSeries

{
  "durada_dels_capiols" : "25 min",
  "primer_episodi : "1r abril 1975",
  "ultim_episodi : "20 abril 1976",
  "temporades" : 2,
  "episodis : 104,
}




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

