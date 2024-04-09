Quotes to Scrape<a name="TOP"></a>
===================

This project is developed to scrape on the [Quotes to Scrape](http://quotes.toscrape.com/) website,
and return the desired information then save it to a txt file.
This project has three spiders to scrape and extract for quotes, authors, and tags.
Note: Using this website is prohibited in Iran.

- - - -

### Python and package used:
Name  | Version
-------- | --------
Python | 3.12.0
Scrapy | 2.11.1

### How to use:
1- To use each of the spiders, uncomment the corresponding pipeline in the settings.py file.
```
settings.py


ITEM_PIPELINES = {
   # "quotes_to_scrape.pipelines.QuotesPipeline": 300,
   # "quotes_to_scrape.pipelines.AuthorsPipeline": 300,
   # "quotes_to_scrape.pipelines.TagsPipeline": 300,
}
```
2- Navigate to the spiders directory path and run the desired spider.
```
>>> scrapy runspider [spider name]
```
