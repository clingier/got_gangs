import scrapy
from . import CHARACTERS
from bs4 import BeautifulSoup

class GotSpider(scrapy.Spider):
    name = 'got'
    links_cached = set()

    def stat_requests(self):
        urls = [
            'https://gameofthrones.fandom.com/wiki/Game_of_Thrones_Wiki'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def __is_a_link_to_fandom(self, link):
        return True
    
    def get_all_links(self, response):
        """Fetch all links that stay in the Fandom from the spider response.
        get_all_links make sure that the links aren't previously visited.
        """
        return []
    
    def get_characters_from_pages(self, response):
        """Builds the list of characters cited in the fandom page."""
        return []
    
    def parse(self, response):
        """Builds the characters list cited in the response and fetch all links.
        After every link are visited parse make sure to add it in the cache.
        """
        print(response)