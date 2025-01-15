import requests
from bs4 import BeautifulSoup
import json
import os

url = "https://www.poe2wiki.net/wiki/Mace"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Example: Extract all paragraph texts
# spans = soup.find_all('span', class_='c-item-hoverbox__activator')
tds = soup.find_all('td')
all_jawns = {}
for jawn in tds:
    img_path = 'https://www.poe2wiki.net'
    temp_jawn = {}
    span = jawn.find('span', class_='c-item-hoverbox__activator')
    if span:
        item_name = span.find('a').get_text()
        img_span = span.find('span')
        if img_span:
            print("poop!")
            img_tag = img_span.find('a')
            if img_tag:
                img_tag = img_tag.find('img')
            if img_tag:
                img_path += img_tag['src']
    if item_name not in all_jawns:
        all_jawns[item_name] = img_path 
    img_path = 'https://www.poe2wiki.net'
    temp_jawn = {}

with open('maces.json', 'w') as fp:
    json.dump(all_jawns, fp)





# import scrapy
# import json


# class QuotesSpider(scrapy.Spider):
#     name = "mace"
#     start_urls = [
#         "https://www.poe2wiki.net/wiki/Mace",
#     ]

#     def parse(self, response):
#         with open('responseShit.json', 'a') as f:
#             for item in response.css("c-item-hoverbox__activator"):
#                 entry = {
#                     "item_name": item.xpath("a.text()").get(),
#                     "image_path": item.css("span > span > a > img::attr('src')").get(),
#                 }
#                 f.write(json.dumps(entry) + '\n')

