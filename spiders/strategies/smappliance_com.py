from .base import SpiderStrategy
from ..helpers import convert_price_to_float
import logging
import requests
from bs4 import BeautifulSoup
import time

class SmapplianceComStrategy(SpiderStrategy):
    def __init__(self, url):
        self.url = url
        self.logger = logging.getLogger(__name__)
   
    def _download(self, headers=None, cookies=None, timeout=10, data=None):
        response = None
        try:  
            payload = {}
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'if-none-match': '"cacheable:4bdc2be1dfb3be16c169c582113684c8"',
                'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
            }

            response = requests.request("GET", self.url, headers=headers, data=payload) 
            if response.status_code == 200:
                if not response.history: 
                    return response.text
                else:
                    return None
            
        except Exception as e:
            self.logger.exception(e)
        return response
    
    def execute(self):
        products_list = []
        next_page_number = 2
        base_url = self.url
        while True:
            print(f'\t[+]Page: {self.url}')
            raw_data = self._download()
            if raw_data:
                soup = BeautifulSoup(raw_data, 'lxml')
                product_tags = soup.select('.product-list.product-list--collection > div.product-item')
                next_page = f'{base_url}?page={next_page_number}' if product_tags else None
                print(f'\t[+]Products: {len(product_tags)}') 
                if product_tags:
                    for product_tag in product_tags:
                        data = {}
                        data['title'] = self._get_title(product_tag)
                        data['url'] = self._url(product_tag)
                        data['price'] = self._get_price(product_tag)
                        data['image_url'] = self._image_url(product_tag)
                        data['brand'] = self._brand(product_tag)
                        products_list.append(data)
                if next_page:
                    self.url = next_page
                    next_page_number += 1
                    time.sleep(10)
                else:
                    break
            else:
                print('\t[!]Download Failed')
                break
        print(f'\t[+]Total Products: {len(products_list)}') 
        return products_list

    def _get_title(self, product_tag: BeautifulSoup):
        value = 'NOT_FOUND'

        try:
            title_tag = product_tag.select_one('a.product-item__title')
            if title_tag:
                value = title_tag.get_text()
        except Exception as e:
            value = 'FAILED'
            self.logger.exception(e)

        return str(value)

    def _url(self, product_tag: BeautifulSoup):
        value = 'NOT_FOUND'

        try:
            url_tag = product_tag.select_one('a.product-item__title')
            if url_tag and url_tag.has_attr('href'):
                value = f'https://www.smappliance.com{url_tag['href']}'
        except Exception as e:
            value = 'FAILED'
            self.logger.exception(e)

        return str(value)

    def _get_price(self, product_tag: BeautifulSoup):
        value = 0.0

        try:
            price_tag = product_tag.select_one('.price.price--highlight')
            if price_tag:
                value = convert_price_to_float(price_tag.get_text())
        except Exception as e:
            value = 0.0
            self.logger.exception(e)

        return value

    def _image_url(self, product_tag: BeautifulSoup):
        value = 'NOT_FOUND'

        try:
            image_tag = product_tag.select_one('img.product-item__primary-image')
            if image_tag and image_tag.has_attr('data-src'):
                value = image_tag['data-src'].replace('{width}', '500')
        except Exception as e:
            value = 'FAILED'
            self.logger.exception(e)

        return str(value)
    
    
    def _brand(self, product_tag: BeautifulSoup):
        value = 'NOT_FOUND'

        try:
            brand_tag = product_tag.select_one('a.product-item__vendor')
            if brand_tag:
                value = brand_tag.get_text()
        except Exception as e:
            value = 'FAILED'
            self.logger.exception(e)

        return str(value)