"""
@author JP Zamanillo
@source https://www.proxiesapi.com/blog/scraping-listings-from-realtor-with-python-and-bea.html.php
"""

# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.11 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
    "Accept-Encoding": "identity",
}
#'Accept-Encoding': 'identity'

url = "https://www.realtor.com/realestateandhomes-search/Portland_OR"

response = requests.get(url, headers=headers)

# print(response.content)

soup = BeautifulSoup(response.content, "lxml")


for item in soup.select(".component_property-card"):
    try:
        print("**********")
        # print(item)
        print(item.select("[data-label=pc-price]")[0].get_text())
        print(item.select("img")[0]["data-src"])
        print(item.select(".summary-wrap")[0].get_text())
        print(item.select(".address")[0].get_text())
        print(item.select(".property-meta")[0].get_text())
        print(item.select(".special-feature-list")[0].get_text())

    except Exception as e:
        # raise e
        print("")

