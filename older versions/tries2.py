from lxml import etree
import requests

url = 'https://www.baidu.com'
head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
resp = requests.get(url, headers = head)#.content.decode('utf-8')
e = etree.HTML(resp.text)
info = e.xpath('//div[@id="s-top-left"]/a/text()')
print(info)


url = 'https://www.bing.com'
head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
resp = requests.get(url, headers = head)#.content.decode('utf-8')
print(resp.text)
e = etree.HTML(resp.text)
info = e.xpath('//div[@class="musCardCont"]/h2/a/text()')
print(info)