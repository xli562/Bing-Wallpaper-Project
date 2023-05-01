from urllib import response
from lxml import etree
import requests

url = 'https://www.bing.com'
head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
resp = requests.get(url, headers = head).content.decode('utf-8')

e = etree.HTML(resp)


#getting the link to the image
imgLinkLocation = e.xpath('/html/head/link[@rel="preload"]')
imgLink = imgLinkLocation[0].attrib.get('href')
imgLink = 'https://www.bing.com'+imgLink
print(imgLink)

#requesting the binary data of the image
imgDown = requests.get(imgLink, headers = head)

with open(f'D:/Users/henry/Desktop/Auto downloaded bing wallpaper - to be selected/1.jpg', 'wb') as f:
    f.write(imgDown.content)
