import json
import importlib
from .exceptions import StrategyNotFound
class Factory: 

    SPIDER_SUFFIX = 'Strategy'
    MAP_FILE_PATH = 'spiders/map.json'
    def get_strategy(self, website):
        try:
            with open(self.__class__.MAP_FILE_PATH, 'r') as f:
                mapping = json.load(f)
                file_name = mapping[website]
                spider_module = importlib.import_module(f'spiders.strategies.{file_name}')
                class_name = self._get_class_name(website)
                return getattr(spider_module, class_name) 
        except KeyError:
            raise StrategyNotFound('Strategy not found')
        except:
            raise Exception('Unhandled Exception')
        
    def _get_class_name(self, website): 
        website_parts = website.replace('www.', '').split('.') 
        class_name = ''
        for part in website_parts:
            class_name += part.capitalize() 

        class_name += self.__class__.SPIDER_SUFFIX

        return class_name
         