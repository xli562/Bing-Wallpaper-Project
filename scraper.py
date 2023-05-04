from datetime import datetime, timedelta
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request as request
from comment_image_files import commentJPG


forbiddenChars = ['\\','/',':','*','?','"','<','>','|']  # 9 forbidden chars in WinOS file system
replacmntChars = ['＼','／','：','＊','？','＂','＜','＞','｜']


#with webdriver.Remote(command_executor='http://10.2.9.19:4444', options=webdriver.ChromeOptions()) as browser:
with webdriver.Chrome() as browser:
    browser.get('https://www.bing.com/')
    print('----------------------------------------------')

    # wait for the page to fully load
    WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/div")))
    print('==================================================')

    # Click 'reject all optional cookies'
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'bnp_btn_reject'))).click()

    # try 5 times in getting the link to image
    for i in range(5):
        try:
            # Previous xpath used: /html/body/div[1]/div/div[1]/div[2]/div[2]
            WebDriverWait(browser, 600).until(EC.text_to_be_present_in_element_attribute((By.XPATH, "/html/body/div[3]/div/div[1]/div[2]/div[2]"), 'style', '/th?id=OHR'))
            link = browser.find_element(By.XPATH, value='/html/body/div[3]/div/div[1]/div[2]/div[2]').get_attribute('style')
            link = link[link.index('url("/th?id=OHR.')+5 : link.index('&rf=LaDigue')].replace('1920x1080', 'UHD')
            link = 'https://www.bing.com/' + link + '&qlt=100'
            print(f'image link: \033[32m{link}\033[0m')
            break
        except ValueError:
            raise FileNotFoundError('Image link cannot be found in the html. try manually looking for the image link. it seems that it can change places. make sure it has "qlt" in it')
    

    # getting image descriptions as file name
    fileName = browser.find_element(By.XPATH, '//*[@id="vs_cont"]/div[1]/div[2]/div[1]/h3/a').text
    fileName += f" - {browser.find_element(By.ID, 'headline').text}"
    for i in range(8):
        fileName = fileName.replace(forbiddenChars[i],replacmntChars[i])
    if fileName.startswith(' - ') or fileName.endswith(' - '):
        raise ResourceWarning('File name not complete - try manually looking for the the xpath and replacing the one here (move the present one to comments). it seems that bing xpaths can change places. ')
    print(f'name of file: \033[95{fileName}\033[0\n')
    imgData = request.urlretrieve(link, f'D:/Users/henry/Desktop/Auto downloaded bing wallpaper - to be selected/{fileName}.jpg')


    # getting image comment
    commentLink = browser.find_element(By.XPATH, '//*[@id="vs_cont"]/div[1]/div[2]/div[1]/h3/a').get_attribute('href')
    time.sleep(1)
    print(f'commentlink: \033[32m{commentLink}\033[0m')
    browser.get(commentLink)
    
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'bs-readmore'))).click()
    WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.ID, 'ency_desc_Prom')))
    comment = browser.find_element(By.ID, 'ency_desc_full').get_attribute('data-translation')
    comment = comment.replace('<br>', '\n')
    print(comment)
    commentJPG(f'D:/Users/henry/Desktop/Auto downloaded bing wallpaper - to be selected/{fileName}.jpg', comment)

    print('\033[47============== File saved with comments written! ==============\033[0')