

from lxml import etree as ET
import requests
url = 'https://www.bing.com'
head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
resp = requests.get(url, headers = head)#.content.decode('utf-8')
fp = resp.text

place = fp.find('href="/search?q=Valley+of+the+Moon&form=hpcapt&filters=HpDate:"20230213_0000""')
print('=======',place)

with open(r"D:\MyPythonCodes\test.txt", 'w') as f:
    f.write(fp)

