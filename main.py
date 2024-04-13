from spiders.spider import Spider  
import os
from supabase import create_client, Client

def categories():
    return [
        { 
            # refrigerators
            "category": 2,
            "targets": [
                # {
                #     "retailer": 1,
                #     "website": 'emcor.com.ph', 
                #     "url": 'https://emcor.com.ph/product-category/home-appliance/refrigerator/'
                # },
                # {
                #     "retailer": 2,
                #     "website": 'ansons.ph', 
                #     "url": 'https://ansons.ph/product-category/refrigerator/'
                # },
                # {
                #     "retailer": 3,
                #     "website": 'mangkosme.com', 
                #     "url": 'https://mangkosme.com/collections/bodega-sale-refrigerator'
                # }, 
                # {
                #     "retailer": 4,
                #     "website": 'saversappliances.com.ph', 
                #     "url": 'https://saversappliances.com.ph/product-category/refrigerator-freezer-chiller/'
                # }, 
                # {
                #     "retailer": 5,
                #     "website": 'www.smappliance.com', 
                #     "url": 'https://www.smappliance.com/collections/refrigerators-and-freezers'
                # }, 
                {
                    "retailer": 6,
                    "website": 'western.com.ph', 
                    "url": 'https://western.com.ph/shop/kitchen-appliances/refrigerators/'
                } 
            ]
           
        },
        # { 
        #     # refrigerators
        #     "name": 1,
        #     "targets": [
        #         {
        #             "website": 'ansons.ph',
        #             "url": 'https://ansons.ph/product-category/refrigerator/'
        #         },
        #          {
        #             "website": 'emcor.com.ph',
        #             "url": 'https://emcor.com.ph/product-category/home-appliance/refrigerator/'
        #         } 
        #     ]
           
        # }
    ]

def insert_products(supabase: Client, products: list|dict): 
    try: 
        supabase.table("products").insert(products).execute()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # connect to supabase
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)

    # run spider 
  
    try:

        for category in categories():
            category_name = category['category']
            print(f'[x] scraping for category: {category_name}')
            for target in category['targets']:
                retailer = target['retailer']
                website = target['website']
                url = target['url']
                print(f'[x] scraping for website: {website}') 
                spider = Spider(website, url)
                products = spider.crawl() 
                for product in products:
                    product['category'] = category_name
                    product['retailer'] = retailer
                insert_products(supabase, products)
                
    except Exception as e:
        print(e)




