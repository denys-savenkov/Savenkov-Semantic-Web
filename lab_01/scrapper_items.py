import scrapy

class DjinniItem(scrapy.Item):
    url = scrapy.Field()
    position = scrapy.Field()
    locations = scrapy.Field()
    salary = scrapy.Field()
    years_of_experience = scrapy.Field()
    english_level = scrapy.Field()
    experience = scrapy.Field()
    skills = scrapy.Field()
    highlights = scrapy.Field()
    expectations = scrapy.Field()
