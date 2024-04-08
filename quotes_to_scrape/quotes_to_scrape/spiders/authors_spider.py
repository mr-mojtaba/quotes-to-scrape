import scrapy
from quotes_to_scrape.items import AuthorItem


class AuthorSpider(scrapy.Spider):
    name = "author_spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        # Extracting links with the text "about"
        about_links = response.xpath("//a[text()='(about)']/@href").getall()
        # Following each "about" link
        for link in about_links:
            yield response.follow(link, callback=self.parse_about)

        # Following pagination link
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_about(self, response):
        # Extracting desired information from the "about" link
        item = AuthorItem()
        item['name'] = response.css('div.author-details h3.author-title::text').get()
        item['birthdate'] = response.css('div.author-details > p > span.author-born-date::text').get()
        b_location = response.css('div.author-details > p > span.author-born-location::text').get()
        clean_born_location = b_location.split(" ")[1:]
        clean_born_location = " ".join(clean_born_location)
        item['born_location'] = clean_born_location
        item['description'] = response.css('div.author-details div.author-description::text').get()
        yield item
