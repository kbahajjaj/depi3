import os

spiders = ["quotes", "books", "httpbin"]

for spider in spiders:
    print(f"\n=== Running spider: {spider} ===\n")
    os.system(f"scrapy crawl {spider} -O outputs/{spider}.csv")


# scrapy crawl quotes -O outputs/quotes.csv