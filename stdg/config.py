import configparser
import shopify
import pandas as pd

settings = configparser.ConfigParser()
settings.read('stdg.ini')

store_settings = settings['shopify']
shop_url = "https://%s:%s@%s.myshopify.com/admin" % (
    store_settings['API_KEY'], store_settings['API_PASS'], store_settings['STORE'])
shopify.ShopifyResource.set_site(shop_url)

postal_data = pd.read_csv("zip-codes.txt", header=None, converters={0: lambda x: str(x)})
postal_data.columns = ["postal_code", "lat", "long", "city", "state", "county", "unique"]

# Isolate the two columns we really care about.
postal_data = postal_data[["state","postal_code"]]

# State abbreviations to remove. Shopify does not recognize these states.
# From: US District, Territory, and Possession Abbreviations and Capitals
# http://www.stateabbreviations.us/
for state in ['AS', 'DC', 'FM', 'GU', 'MH', 'MP', 'PW', 'PR', 'VI']:
    postal_data = postal_data[postal_data.state != state]
