import requests
from lxml import etree

response = requests.get("https://ibaotu.com/shipin/")

html = etree.HTML(response.text)
tit_list = html.xpath('//span')