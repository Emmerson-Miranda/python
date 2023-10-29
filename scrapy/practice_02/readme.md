# create a project

```bash
scrapy startproject bookscraper
```

## create spider

```bash
cd ./bookscraper/bookscraper/spiders/
scrapy genspider bookspider books.tocrape.com
```

# run this project

```bash
scrapy runspider qoutes.py -o quotes.json
```

# Source

https://www.youtube.com/watch?v=mBoX_JCKZTE
