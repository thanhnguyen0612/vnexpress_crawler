
import os
import time
import csv
import requests
import json
from bs4 import BeautifulSoup

from model import Article
from output import output, reset

cate_id = "1001014"
data_name = "data"

page_index = 1
page_size  = 50
article_number = 300

def run(spec_url = ""):
    reset()

    if len(spec_url) > 0:
        art = Article()
        art.url = spec_url
        crawlContent(art)
        return

    base_url = "https://gw.vnexpress.net/ar/get_rule_2?data_select=article_id,article_type,title,share_url,thumbnail_url,publish_time,lead,privacy,original_cate,article_category"

    count = 0
    index = page_index

    arts = []
    while count < article_number:
        url = "{0}&category_id={1}&page={2}&limit={3}".format(base_url, cate_id, index, page_size)
        items = crawlLinks(url)

        if items is not None:
            arts.extend(items)
            index += 1

        count += page_size

    output(arts)
    

def crawlLinks(api_url = ""):
    response = requests.get(api_url)
    
    # format json response: {"status": 200, "data": {"1001014": "data": [{...}]}}
    obj = json.loads(response.content)
    if not data_name in obj:
        print(api_url)
        return

    data = obj[data_name]
    if not cate_id in data:
        print(api_url)
        print(obj)

        return
    
    if not data_name in data[cate_id]:
        print(api_url)
        print(data[cate_id])
        return

    items = data[cate_id][data_name]

    arts = []
    for item in items:
        art = Article()
        art.title = item["title"]
        art.lead = item["lead"]
        art.url = item["share_url"]

        print("Article url: {0}".format(art.url))
        crawlContent(art)
        arts.append(art)

    return arts

def crawlContent(art = Article):
    page = requests.get(art.url)

    soup = BeautifulSoup(page.content, "html.parser")
    div = soup.findChild("div", class_="sidebar-1")
    paragraphs = div.find_all("p", "Normal")
    
    if not paragraphs:
        print("Don't have paragraphs, url: {0}".format(art.url))
        return

    if len(paragraphs) > 2:
        paragraphs = paragraphs[:len(paragraphs)-2]

    content = ""
    for para in paragraphs:
        content += toString(para) + "\n"

    art.addContent(content.rstrip("\n"))
    
def toString(tag):
    if tag.string:
        return tag.string
    
    return tag.text