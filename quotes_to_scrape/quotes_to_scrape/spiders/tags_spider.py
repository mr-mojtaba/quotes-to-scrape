import scrapy
from quotes_to_scrape.items import TagsItem


class QuotesSpider(scrapy.Spider):
    name = "tags_spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        # Extracting tags from each quote
        for quote in response.css('div.quote'):
            item = TagsItem()
            item['tags'] = quote.css("div.tags a.tag::text").getall()
            yield item

        # Following the pagination link if available
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
