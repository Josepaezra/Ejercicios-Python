from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from Data_Processing import Cedulas

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"]) #Evita mensaje: un software de prueba automatizado esta controlando chrome
options.add_experimental_option("detach", True) #keep the browser open after the process has ended, so long as the quit command is not sent to the driver.
#Descarga en la carpeta indicada
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\user\Documents\Data Kardex\Ciclo Basico"
  })
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(2)
browser.get('http://mwikicpd.ing.ucv.ve/Kardex_estud/')

No_kardex=[] #Lista para guardar las cédulas sin kardex disponible

for cedula in Cedulas:
    browser.find_element("xpath", "/html/body/div/form/ul/li[1]/span/input").clear()
    caja_usr=browser.find_element("xpath", "/html/body/div/form/ul/li[1]/span/input")
    caja_usr.send_keys(cedula)
    browser.find_element("xpath", "/html/body/div/form/ul/li[2]/input[2]").click()
    #action = webdriver.ActionChains(browser)  #Espera un segundo antes de la proxima acción
    #action.pause(1)
    #action.perform()

    try:
        browser.find_element("xpath", "/html/body/div/form/ul/p/a").click()
        No_kardex.append(cedula)
    except NoSuchElementException:
        pass

print(No_kardex)

""""
    if browser.find_element("xpath","/html/body/div/form/ul/p/a").size() != 0:
        browser.find_element("xpath", "/html/body/div/form/ul/p/a").click()
        No_kardex.append(cedula)
"""
