from selenium import webdriver
import time
import requests 
import re  
from playsound import playsound
import time
from pygame import mixer

import PIL.ImageGrab





chromedriver = "/Users/marci/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get('https://vaccinicovid.regione.veneto.it/ulss9')
first_login = '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a'
fiscale = '//*[@id="cod_fiscale"]'
sanitaria = '//*[@id="num_tessera"]'
login_button = '//*[@id="corpo1"]/div[4]/div[2]/input'
login_submit = '//*[@id="corpo1"]/div[6]/div[2]/button'
sambo = '//*[@id="corpo2"]/button[5]'
a=0
uno = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div/table/tbody/tr[5]/td[5]/div/div[1]/a'

bott = '//*[@id="corpo2"]/button'
while(a == 0):
    try:
        time.sleep(3)
        driver.find_element_by_xpath(fiscale).send_keys("BRNMRC02H12L781R")
        driver.find_element_by_xpath(sanitaria).send_keys("980204")
        driver.find_element_by_xpath(login_button).click()
        driver.find_element_by_xpath(login_submit).click()
    
        time.sleep(3)
        driver.find_element_by_xpath(sambo).click()
        time.sleep(3)
        driver.find_element_by_xpath(uno).click()
    except:
        print("An exception occurred")
        driver.refresh()
 
    try:
        time.sleep(3)
        driver.find_element_by_xpath(bott)
        driver.find_element_by_xpath(bott).click()
        print("fatto")
        a = 1
        im = PIL.ImageGrab.grab()
        im.show()
    except:
        print("An exception occurred")
        driver.refresh()
  


try:
    driver.find_element_by_xpath('//*[@id="corpo1"]/div[4]/div[2]/input').send_keys("brunelli")
    driver.find_element_by_xpath('//*[@id="corpo1"]/div[5]/div[2]/input').send_keys("marco")
    driver.find_element_by_xpath('//*[@id="corpo1"]/div[5]/div[2]/input').send_keys("marcibr20@gmail.com")
    driver.find_element_by_xpath('//*[@id="corpo1"]/div[5]/div[2]/input').send_keys("3475941419")
    driver.find_element_by_xpath('//*[@id="bottoneconferma"]').click()
except:
    im = PIL.ImageGrab.grab()
    im.show()
    
mixer.init()
mixer.music.load("/Users/marci/Downloads/file_example_MP3_5MG.mp3")
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(100)