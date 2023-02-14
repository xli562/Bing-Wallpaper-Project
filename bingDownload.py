# Maybe use exif
# 搞清楚自定义函数内的变量到底能不能被外部使用，以及自定义函数能否使用上文定义过的外部变量
from lxml import etree
import requests
from time import sleep

head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
endStatus = {'Place_info_not_found': False, 'Short_discription_not_found': False,'Long_description_not_found': False, 'Image_not_found': False}

def getRoot():
    '''Returns the element-tree root of the website.'''
    
    url = 'https://www.bing.com'
    resp = requests.get(url, headers = head)
    root = etree.HTML(resp.text)
    return root

def getTitle(endStatus: dict) -> str:
    '''Returns the file name aka title of the image. Will change values 
    in the "endStatus" dict that calls attention at the end of the program 
    if something cannot be fetched, and should be fetched manually in the browser.'''
    
    # Initializing variables
    forbiddenChars = ['\\','/',':','*','?','"','<','>','|']  # 9 forbidden chars in WinOS file system
    replacmntChars = ['＼','／','：','＊','？','＂','＜','＞','｜']
    imgTitle1 = ""
    imgTitle2 = ""

    # Getting the place info of the image
    try:
        imgTitle1_asList = root.xpath("//*[@id='headline']/text()")
        imgTitle1 = str(imgTitle1_asList[0])
    except IndexError:
        endStatus['Place_info_not_found'] = True
    
    # Getting the short discription of the image
    try:
        imgTitle2_asList = root.xpath("//*[@id='vs_cont']/div[1]/div[2]/div[1]/h2[1]/a[1]/text()")
        print(imgTitle2_asList)
        imgTitle2 = str(imgTitle2_asList[0])
    except IndexError:
        endStatus['Short_discription_not_found'] = True
    
    # Combining to get the image title
    imgTitle = imgTitle1+' - '+imgTitle2

    #Replacing the forbidden chars
    for i in range(8):
        imgTitle = imgTitle.replace(forbiddenChars[i],replacmntChars[i])
    
    return imgTitle

def getDscrptn(endStatus) -> str:
    '''Getting long description to the image.'''

    imgDscrptn = ''
    try:
        imgDscrptn_asList = root.xpath('//span[@class="text"]/text()')
        imgDscrptn = str(imgDscrptn_asList[0])
        print(imgDscrptn)
    except IndexError:
        endStatus['Long_description_not_found'] = True
    
    return imgDscrptn

def getImgData(endStatus) -> bytes:
    '''Returns the image data as bytes.'''

    try: 
        imgLinkLocation = root.xpath('/html/head/link[@rel="preload"]')
        imgLink = imgLinkLocation[0].attrib.get('href')
        imgLink = 'https://www.bing.com'+imgLink
        print(imgLink)
        # Requesting the binary data of the image
        imgDown = requests.get(imgLink, headers = head)
    except IndexError:
        endStatus['Image_not_found'] = True
    
    return imgDown

def happyEnding(endStatus) -> None:
    for value in endStatus.values():
        if value == True:
            endHalt = True
            break
    if endHalt == True:
        print("These data below are not found:")
        for key in endStatus:
            if endStatus[key] == True:
                print(key)
                print()
        input("Please get these data as you would in the old days.")


root = getRoot()
imgTitle = getTitle(endStatus)
imgDscrptn = getDscrptn(endStatus)
imgDown = getImgData(endStatus)

print(imgTitle, imgDscrptn, endStatus)

# Writing into the image file
with open(f'D:/Users/henry/Desktop/Auto downloaded bing wallpaper - to be selected/{imgTitle}.jpg', 'wb') as f:
    f.write(imgDown.content)

# Creating the image description txt file
with open(f'D:/Users/henry/Desktop/Auto downloaded bing wallpaper - to be selected/{imgTitle}.txt', 'a') as f:
    f.write(imgDscrptn)

happyEnding(endStatus)