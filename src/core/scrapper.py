from selenium.webdriver import Firefox , FirefoxOptions
from selenium.webdriver.common.by import By
from .downloader import AparatDownloader
import time



class Aparat:
    def __init__(self,url,path):
        self.url = url
        self.path = path

        
        options = FirefoxOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        # put geckodriver in: /usr/bin or /usr/local/bin
        browser = Firefox(options=options)

        browser.get(url)
        time.sleep(25)
        vid_name = browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[1]/h1/span').text
        browser.find_element(By.CLASS_NAME,'sc-38580b3-0 jrFCUR button icon-button').click() # ... button
        time.sleep(1)
        browser.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/div/div/ul/li[1]/button').click() # download button
        time.sleep(1)
        quality_btn = browser.find_element(By.XPATH,'//*[@id="144p"]')
        vid_lnk = quality_btn.get_property('href')



        video = AparatDownloader(url=vid_lnk,name=vid_name,path=path).download()

        browser.close()
