from spiders.spider import Spider  
import os
from supabase import create_client, Client

def categories():
    return [
         { 
            # airconditioners
            "category": 1,
            "targets": [
                # {
                #     "retailer": 1,
                #     "website": 'emcor.com.ph', 
                #     "url": 'https://emcor.com.ph/product-category/home-appliance/air-conditioners/'
                # },
                # {
                #     "retailer": 2,
                #     "website": 'ansons.ph', 
                #     "url": 'https://ansons.ph/product-category/air-conditioners/'
                # },
                # {
                #     "retailer": 3,
                #     "website": 'mangkosme.com', 
                #     "url": 'https://mangkosme.com/collections/bodega-sale-aircon'
                # }, 
                # {
                #     "retailer": 4,
                #     "website": 'saversappliances.com.ph', 
                #     "url": 'https://saversappliances.com.ph/product-category/air-conditioner-cooling/'
                # }, 
                # {
                #     "retailer": 5,
                #     "website": 'www.smappliance.com', 
                #     "url": 'https://www.smappliance.com/collections/air-conditioner'
                # }, 
                # {
                #     "retailer": 6,
                #     "website": 'western.com.ph', 
                #     "url": 'https://western.com.ph/shop/air-cooling/air-conditioners/'
                # } 
            ]
        },
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
                # {
                #     "retailer": 6,
                #     "website": 'western.com.ph', 
                #     "url": 'https://western.com.ph/shop/kitchen-appliances/refrigerators/'
                # } 
            ]
        }, 
        { 
            # washing machines
            "category": 3,
            "targets": [
                {
                    "retailer": 1,
                    "website": 'emcor.com.ph', 
                    "url": 'https://emcor.com.ph/product-category/home-appliance/small-appliances/'
                },
                {
                    "retailer": 2,
                    "website": 'ansons.ph', 
                    "url": 'https://ansons.ph/product-category/small-appliance/'
                },
                {
                    "retailer": 3,
                    "website": 'mangkosme.com', 
                    "url": 'https://mangkosme.com/collections/bodega-sale-small-appliances'
                }, 
                {
                    "retailer": 4,
                    "website": 'saversappliances.com.ph', 
                    "url": 'https://saversappliances.com.ph/product-category/kitchen-appliances/'
                }, 
                {
                    "retailer": 5,
                    "website": 'www.smappliance.com', 
                    "url": 'https://www.smappliance.com/collections/small-kitchen-appliances'
                }, 
                {
                    "retailer": 6,
                    "website": 'western.com.ph', 
                    "url": 'https://western.com.ph/shop/small-appliances/'
                } 
            ]
        },
        { 
            # televisions
            "category": 4,
            "targets": [
                # {
                #     "retailer": 1,
                #     "website": 'emcor.com.ph', 
                #     "url": 'https://emcor.com.ph/product-category/video/'
                # },
                # {
                #     "retailer": 2,
                #     "website": 'ansons.ph', 
                #     "url": 'https://ansons.ph/product-category/television/'
                # },
                # {
                #     "retailer": 3,
                #     "website": 'mangkosme.com', 
                #     "url": 'https://mangkosme.com/collections/televisions'
                # }, 
                # {
                #     "retailer": 4,
                #     "website": 'saversappliances.com.ph', 
                #     "url": 'https://saversappliances.com.ph/product-category/televisions/'
                # }, 
                # {
                #     "retailer": 5,
                #     "website": 'www.smappliance.com', 
                #     "url": 'https://www.smappliance.com/collections/tv'
                # }, 
                # {
                #     "retailer": 6,
                #     "website": 'western.com.ph', 
                #     "url": 'https://western.com.ph/shop/tv-entertainment/televisions/'
                # } 
            ]
        },
        { 
            # washing machines
            "category": 5,
            "targets": [
                # {
                #     "retailer": 1,
                #     "website": 'emcor.com.ph', 
                #     "url": 'https://emcor.com.ph/product-category/home-appliance/washing-machines/'
                # },
                # {
                #     "retailer": 2,
                #     "website": 'ansons.ph', 
                #     "url": 'https://ansons.ph/product-category/washing-machine/'
                # },
                # {
                #     "retailer": 3,
                #     "website": 'mangkosme.com', 
                #     "url": 'https://mangkosme.com/collections/bodega-sale-washing-machine'
                # }, 
                # {
                #     "retailer": 4,
                #     "website": 'saversappliances.com.ph', 
                #     "url": 'https://saversappliances.com.ph/product-category/washer-dryer/'
                # }, 
                # {
                #     "retailer": 5,
                #     "website": 'www.smappliance.com', 
                #     "url": 'https://www.smappliance.com/collections/washers-and-dryers'
                # }, 
                # {
                #     "retailer": 6,
                #     "website": 'western.com.ph', 
                #     "url": 'https://western.com.ph/shop/washers-dryers/'
                # } 
            ]
        }
        
    ]

def insert_products(supabase: Client, products: list|dict): 
    try:
        print(f'[x] inserting {len(products)} products')
        supabase.table("products").insert(products).execute()
    except Exception as e:
        print(e)
    print(f'[x] done')

def start_crawling(supabase: Client): 
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

if __name__ == '__main__':

    try:
        # connect to supabase
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        spider_email = os.environ.get("SPIDER_EMAIL")
        spider_password = os.environ.get("SPIDER_PASSWORD")
        supabase: Client = create_client(url, key)
        supabase.auth.sign_in_with_password({"email": spider_email, "password": spider_password})  
        # run spider
        start_crawling(supabase)
    except Exception as e:
        print(e)
    finally: 
        supabase.auth.sign_out()
        print('[x] done')








