import scrapy
from . import CHARACTERS

class GotSpider(scrapy.Spider):
    name = 'got'

    def stat_requests(self):
        urls = [
            'https://gameofthrones.fandom.com/wiki/Game_of_Thrones_Wiki'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        print(response)