import configparser
import shopify

settings = configparser.ConfigParser()
settings.read('stdg.ini')

store_settings = settings['shopify']
shop_url = "https://%s:%s@%s.myshopify.com/admin" % (
    store_settings['API_KEY'], store_settings['API_PASS'], store_settings['STORE'])
shopify.ShopifyResource.set_site(shop_url)
