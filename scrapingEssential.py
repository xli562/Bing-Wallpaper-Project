from lxml import etree
import requests

path = "/html/body/div[@class='hpapp']/div[@class='hp_body  ']/div[@class='hpl'][3]/div[@class='bottom_row widget msnpeek']/div[@id='scroll_cont']/div[@id='vs_cont']/div[@class='mc_caro']/div[@class='musCard']/div[@class='headline']/div[@class='icon_text']/a/h1[@id='headline']"
url = 'https://www.bing.com'
head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
resp = requests.get(url, headers = head)#.content.decode('utf-8')

root = etree.HTML(resp.text)

imgTitle1_asList = root.xpath(path)
print(imgTitle1_asList)

# The problem is perhaps the initial page of bing that can be ontained by clearing cache - or, packing cache into the request can perhaps fix the problem as well.