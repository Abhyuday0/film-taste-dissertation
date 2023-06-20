import scrapy


class InceptionItem(scrapy.Item):
    title = scrapy.Field()
    rating = scrapy.Field()
    description = scrapy.Field()

class InceptionSpider(scrapy.Spider):
    name = "inception"
    start_urls = [
        "https://www.imdb.com/title/tt1375666/"
    ]

    def parse(self, response):
        item = InceptionItem()
        item["title"] = response.css("div.title_wrapper h1::text").get().strip()
        item["rating"] = response.css("span.imdb-rating-value::text").get().strip()
        item["description"] = response.css("div.summary_text::text").get().strip()
        yield item
