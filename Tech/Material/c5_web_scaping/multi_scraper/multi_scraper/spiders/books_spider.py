import scrapy
from bs4 import BeautifulSoup
from multi_scraper.items import GenericItem

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/page-1.html"]

    # عدد الصفحات المسموح
    max_pages = 3  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page_count = 0  # عداد الصفحات اللي تمت زيارتها

    def parse(self, response):
        self.page_count += 1
        soup = BeautifulSoup(response.text, "html.parser")

        # استخراج الكتب
        for card in soup.select("article.product_pod"):
            a = card.select_one("h3 a")
            title = a.get("title") if a else None
            price_el = card.select_one("p.price_color")
            price = price_el.get_text(strip=True) if price_el else None
            href = a.get("href") if a else None
            url = response.urljoin(href) if href else response.url

            yield GenericItem(
                title=title,
                author=None,
                price=price,
                tags=[],
                rating=None,
                url=url
            )

        # Pagination مع شرط الحد الأقصى
        if self.page_count < self.max_pages:
            next_link = soup.select_one("li.next a")
            if next_link and next_link.get("href"):
                yield response.follow(next_link.get("href"), callback=self.parse)