from selenium import webdriver 
import time
import PIL.ImageGrab
from webdriver_manager.chrome import ChromeDriverManager
import winsound

#inserire questi dati
#########
sito_ulss = "https://vaccinicovid.regione.veneto.it/ulss9"
codice_fiscale = ""
tessera_sanitaria = ""
nome = ""
cognome = ""
mail = ""
numero = ""
data = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div/table/tbody/tr[5]/td[5]/div/div[1]/a' #copy_xpath
centro_vaccinale = '//*[@id="corpo2"]/button[5]'
##########


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(sito_ulss)
first_login = '//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a'
fiscale = '//*[@id="cod_fiscale"]'
sanitaria = '//*[@id="num_tessera"]'
login_button = '//*[@id="corpo1"]/div[4]/div[2]/input'
login_submit = '//*[@id="corpo1"]/div[6]/div[2]/button'
a=0
bott = '//*[@id="corpo2"]/button'

while(a == 0):
    try:
        time.sleep(3)
        driver.find_element_by_xpath(fiscale).send_keys(codice_fiscale)
        driver.find_element_by_xpath(sanitaria).send_keys(tessera_sanitaria)
        driver.find_element_by_xpath(login_button).click()
        driver.find_element_by_xpath(login_submit).click()
    
        time.sleep(3)
        driver.find_element_by_xpath(centro_vaccinale).click()
        time.sleep(3)
        driver.find_element_by_xpath(data).click()
    except:
        print("An exception occurred")
        driver.refresh()
 
    try:
        time.sleep(3)
        driver.find_element_by_xpath(bott)
        driver.find_element_by_xpath(bott).click()
        print("fatto")
        a = 1
    except:
        print("An exception occurred")
        driver.refresh()
  


try:
    driver.find_element_by_xpath('//*[@id="corpo1"]/div[4]/div[2]/input').send_keys(cognome)
    driver.find_element_by_xpath('//*[@id="corpo1"]/div[5]/div[2]/input').send_keys(nome)
    driver.find_element_by_xpath('//*[@id="corpo1"]/div[6]/div[2]/input').send_keys(mail)
    driver.find_element_by_xpath('//*[@id="corpo1"]/div[7]/div[2]/input').send_keys(numero) 
    driver.find_element_by_xpath('//*[@id="bottoneconferma"]').click()
except:
    im = PIL.ImageGrab.grab()
    im.show()

print("prenotato")
while(True):
    winsound.Beep(2000, 500)
    time.sleep(2)
