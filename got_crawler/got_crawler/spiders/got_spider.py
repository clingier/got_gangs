import scrapy
from . import CHARACTERS
from bs4 import BeautifulSoup

BASE_URL = 'https://gameofthrones.fandom.com/'

class GotSpider(scrapy.Spider):
    name = 'got'
    links_cached = set()

    def start_requests(self):
        url = 'https://gameofthrones.fandom.com/wiki/Game_of_Thrones_Wiki'
        yield scrapy.Request(url=url, callback=self.parse)
    
    def __link_to_fandom(self, link):
        return link[0:6] == '/wiki/'
    
    def get_all_links(self, response):
        """Fetch all links that stay in the Fandom from the spider response.
        get_all_links make sure that the links aren't previously visited.
        """
        links = set(x.get() for x in response.css('a::attr(href)') if self.__link_to_fandom(x.get()))
        links = links.difference(self.links_cached)
        return links
    
    def get_characters_from_pages(self, response):
        """Builds the list of characters cited in the fandom page."""
        soup = BeautifulSoup(response.text, 'html.parser')
        soup = soup.get_text()
        words = set(re.findall('([A-Z][a-z]+)', soup))
        return [w for w in words if w in CHARACTERS]
        
    
    def parse(self, response):
        """Builds the characters list cited in the response and fetch all links.
        After every link are visited parse make sure to add it in the cache.
        """
        self.logger.info('Parse function called on %s', response.url)


        # Following Links
        links = self.get_all_links(response)
        for l in links:
            yield scrapy.Request(BASE_URL + l, callback=self.parse)

        self.links_cached = self.links_cached.union(links)