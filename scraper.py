from datetime import datetime, timedelta
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request as request
import pickle


forbiddenChars = ['\\','/',':','*','?','"','<','>','|']  # 9 forbidden chars in WinOS file system
replacmntChars = ['＼','／','：','＊','？','＂','＜','＞','｜']


#with webdriver.Remote(command_executor='http://10.2.9.19:4444', options=webdriver.ChromeOptions()) as browser:
with webdriver.Chrome() as browser:

    # load cookies
    with open('cookies.pkl', 'rb') as f:
        cookies = pickle.load(f)
        browser.get('https://www.bing.com/')
        browser.add_cookie(cookies)


    browser.get('https://www.bing.com/')
    WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located)

    # try 5 times in getting the link to image
    for i in range(5):
        try:
            link = browser.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div[2]/div[2]').get_attribute('style')
            link = link[link.index('url("/th?id=OHR.')+5 : link.index('&rf=LaDigue')].replace('1920x1080', 'UHD')
            link = 'https://www.bing.com/' + link + '&qlt=100'
            print(link)
            break
        except ValueError:
            pass
    time.sleep(10)

    # stores cookies
    cookies = browser.get_cookies()
    for cookie in cookies:
        cookie['expiry'] = 1717177625
    with open('cookies.pkl', 'wb') as f:
        pickle.dump(cookies, f)

    
    # getting image descriptions as file name
    fileName = browser.find_element(By.CLASS_NAME, 'title').text
    fileName += f" - {browser.find_element(By.ID, 'headline').text}"
    for i in range(8):
        fileName = fileName.replace(forbiddenChars[i],replacmntChars[i])
    print(fileName)
    imgData = request.urlretrieve(link, f'{fileName}.jpg')

    time.sleep(1)

    # getting image comment
    print(browser.find_element(By.CLASS_NAME, 'title').text)
    #commentLink = 'https://www.bing.com'+browser.find_element(By.CLASS_NAME, 'title').get_attribute('href')
    #print(commentLink)
    assert 0
    
    WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located)
    browser.find_element(By.ID, 'bs-readmore')
    comment = browser.find_element(By.ID, 'ency_desc_Prom')
    print(comment)