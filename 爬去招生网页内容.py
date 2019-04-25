import requests
import urllib.request
from bs4 import BeautifulSoup

word='山东大学+港澳台+本科生+简章'#在百度上查关键词为‘梁左嘉懿’的网页
# url_values=urllib.parse.urlencode(data)#urlencode:把普通字符串转化为url格式
# 含中文需要用urllib.parse.quote防止报错
tw='edu.cn'
url = 'http://www.xmu.edu.cn/'
# url ='http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd='+urllib.parse.quote(word)+'&oq=%25E5%25B1%25B1%25E4%25B8%259C%25E5%25A4%25A7%25E5%25AD%25A6%2520%25E6%25B8%25AF%25E6%25BE%25B3%25E5%258F%25B0%2520%25E7%25AE%2580%25E7%25AB%25A0&rsv_pq=b5ae7a5400006d82&rsv_t=ba48YGCqXRaRaMnbbZ030EzIWI4J%2FSRle0Cj2hE9uSOdStZa378EG%2FDf8iU&rqlang=cn&rsv_enter=0&inputT=7367&si=edu.cn&ct=2097152'

response = urllib.request.urlopen(url)
page = response.read()
print(page)
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Encoding': 'gzip, deflate, compress',
#     'Accept-Language': 'en-us;q=0.5,en;q=0.3',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
# }
#
# all = open('D:\\111\\test.xlsx', 'a')
soup = BeautifulSoup(page,'lxml')
# print(soup)
href = soup.find_all('li', limit=1)
print(href)
# baidu_url =requests.get(url=href, headers=headers, allow_redirects=False)
# real_url = baidu_url.headers['Location']  #得到网页原始地址
# if real_url.startswith('http'):
#     all.write(real_url + '\n')


