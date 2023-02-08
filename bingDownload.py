'''
exif
'''
from urllib import response
from lxml import etree
from matplotlib.streamplot import interpgrid
import requests

url = 'https://www.bing.com'
head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
resp = requests.get(url, headers = head).content.decode('utf-8')
forbiddenChars = ['\\','/',':','*','?','"','<','>','|']  #9 forbidden chars in WinOS file system
replacmntChars = ['＼','／','：','＊','？','＂','＜','＞','｜']

e = etree.HTML(resp)

#getting the file name aka title of the image
imgTitle1_asList = e.xpath('//div[@class="musCardCont"]/h2/a/text()')
imgTitle1 = str(imgTitle1_asList[0])
imgTitle2_asList = e.xpath('//div[@class="icon_text"]/a/h1/text()')
imgTitle2 = str(imgTitle2_asList[0])
imgTitle = imgTitle1+' - '+imgTitle2
for i in range(8):
    imgTitle = imgTitle.replace(forbiddenChars[i],replacmntChars[i])

#getting the link to the image
imgLinkLocation = e.xpath('/html/head/link[@rel="preload"]')
imgLink = imgLinkLocation[0].attrib.get('href')
imgLink = 'https://www.bing.com'+imgLink
print(imgLink)

#requesting the binary data of the image
imgDown = requests.get(imgLink, headers = head)

with open(f'D:/Users/henry/Desktop/Auto downloaded bing wallpaper - to be selected/{imgTitle}.jpg', 'wb') as f:
    f.write(imgDown.content)

#creating the image description txt file
with open(f'D:/Users/henry/Desktop/Auto downloaded bing wallpaper - to be selected/{imgTitle}.txt', 'a') as f:
    f.write('')