from .factory import Factory

class Spider: 
    def __init__(self, website, url):
        factory = Factory()
        self.strategy = factory.get_strategy(website)(url)
 
    def crawl(self):
        return self.strategy.execute()