import scrapy
from bs4 import BeautifulSoup
from multi_scraper.items import GenericItem

class HttpBinSpider(scrapy.Spider):
    name = "httpbin"
    allowed_domains = ["httpbin.org"]
    start_urls = ["https://httpbin.org/html"]

    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")

        h1_text = soup.select_one("h1").get_text(strip=True)
        first_p = soup.select_one("p").get_text(strip=True)

        yield GenericItem(
            title=h1_text,
            author=None,
            price=None,
            tags=[first_p],
            rating=None,
            url=response.url
        )
