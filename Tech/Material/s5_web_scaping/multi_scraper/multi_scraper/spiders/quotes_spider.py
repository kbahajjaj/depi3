import scrapy
from bs4 import BeautifulSoup
from multi_scraper.items import GenericItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/page/1/"]

    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
                        # soup.find_all("div", class_ = "quote" )
                         # soup.find("div", class_ = "quote" )
        for quote_div in soup.select("div.quote"):
            text = quote_div.select_one("span.text").get_text(strip=True)
            author = quote_div.select_one("small.author").get_text(strip=True)
            tags = [t.get_text(strip=True) for t in quote_div.select("div.tags a.tag")]

            yield GenericItem(
                title=text,
                author=author,
                price=None,
                tags=tags,
                rating=None,
                url=response.url
            )

        # Pagination
        next_link = soup.select_one("li.next a")
        if next_link:
            yield response.follow(next_link.get("href"), callback=self.parse)
