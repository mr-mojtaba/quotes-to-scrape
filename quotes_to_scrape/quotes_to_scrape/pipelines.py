# Define your item pipelines here

# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


class QuotesPipeline:
    def process_item(self, item, spider):
        # Append quote information to quotes.txt file
        with open('quotes.txt', 'a', encoding='utf-8') as f:
            f.write(f'Quote {item["noq"]}: {item["text"]}\n'
                    f'Author: {item["author"]}\n'
                    f'Tags: {item["tags"]}\n\n')
        return item


class AuthorsPipeline:
    def process_item(self, item, spider):
        # Append author information to authors.txt file
        with open('authors.txt', 'a', encoding='utf-8') as f:
            f.write(f'Name: {item["name"]}\n'
                    f'Birthdate: {item["birthdate"]}\n'
                    f'Born location: {item["born_location"]}\n'
                    f'Description: {item["description"]}\n')
        return item


class TagsPipeline:
    def __init__(self):
        # Open tags.txt file in append mode
        self.tags_file = open('tags.txt', 'a', encoding='utf-8')
        # Create an empty set to store unique tags
        self.tags = set()

    def process_item(self, item, spider):
        # Extract tags from item and update the tags set
        tags = item.get('tags')
        if tags:
            self.tags.update(tags)
        return item

    def close_spider(self, spider):
        # Write unique tags to tags.txt file
        for tag in self.tags:
            self.tags_file.write(tag + '\n')
        # Close tags.txt file
        self.tags_file.close()
