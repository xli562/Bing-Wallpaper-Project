from lxml import etree
import requests

url = 'https://www.bing.com'
head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
resp = requests.get(url, headers = head)

root = etree.HTML(resp.text)

imgTitle1_asList = root.xpath("//*[@id='headline']/text()")
print(imgTitle1_asList)




# The problem is perhaps the initial page of bing that can be ontained by clearing cache - or, packing cache into the request can perhaps fix the problem as well