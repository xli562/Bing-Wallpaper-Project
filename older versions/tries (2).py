from lxml import etree
import requests
url = 'https://www.bing.com'
head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
page = requests.get(url, headers=head)

root = etree.HTML(page.text)

cont = root.findall(".//*[@data-h='ID=HpApp,21421.1']")
print(root)