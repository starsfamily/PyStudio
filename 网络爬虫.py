# -*- coding: utf-8 -*-
"""
Crawler

@author: Dazhuang
"""
import requests
from bs4 import BeautifulSoup
import re

s = 0
r = requests.get('https://book.douban.com/subject/30360179/comments/')
soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('span', 'short')  # 之前此处标签为'p', 'comment-content'
for item in pattern:
    print(item.string)
pattern_s = re.compile('<span class="user-stars allstar(.*?) rating"')
p = re.findall(pattern_s, r.text)
for star in p:
    s += int(star)
print(s)