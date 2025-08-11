import scrapy

class GenericItem(scrapy.Item):
    title = scrapy.Field()     # Quote text OR Book title OR HttpBin <h1>
    author = scrapy.Field()    # Quote author (or None)
    price = scrapy.Field()     # Book price (or None)
    tags = scrapy.Field()      # List of tags (or [])
    rating = scrapy.Field()    # Book rating text like 'Three' (or None)
    url = scrapy.Field()       # Source page URL
    scraped_at = scrapy.Field()  

