# Scrapy settings for multi_scraper project

BOT_NAME = "multi_scraper"

SPIDER_MODULES = ["multi_scraper.spiders"]
NEWSPIDER_MODULE = "multi_scraper.spiders"

ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 0.5  # Small politeness delay

# Keep it minimal. We'll output via -O on the CLI.
# If you want logs, uncomment the next two lines:
# LOG_FILE = "logs/multi_scraper.log"
# LOG_LEVEL = "INFO"

DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en",
    # Simple UA to avoid being blocked by trivial filters
    "User-Agent": "Mozilla/5.0 (compatible; MultiScraperBot/1.0; +https://example.com/bot)"
}

ITEM_PIPELINES = {
    "multi_scraper.pipelines.AddTimestampPipeline": 200,

}

