import scrapy
from quotes_to_scrape.items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    # Variable for counting the number of quotes
    number = 0

    def parse(self, response):
        # Iterate over each quote on the page
        for quote in response.css('div.quote'):
            # Increment the quote number
            self.number += 1

            # Create a new instance of QuotesItem class
            item = QuotesItem()

            # Set the attributes of the quote
            item['noq'] = self.number
            item['text'] = quote.css('span.text::text').get()
            item['author'] = quote.css('span small::text').get()
            item['tags'] = quote.css("div.tags a.tag::text").getall()

            # Yield the item as output
            yield item

        # Following the pagination link if available
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
