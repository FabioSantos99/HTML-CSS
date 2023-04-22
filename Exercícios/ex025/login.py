from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep




navegador = webdriver.Chrome()

navegador.get("https://forum.gatapop.com/")

navegador.find_element(By.XPATH,'//*[@id="elUserSignIn"]').click()

navegador.find_element(By.ID, 'auth').send_keys("ZeLove")
navegador.find_element(By.ID, 'password').send_keys("Camis@100")
navegador.find_element(By.XPATH, '//*[@id="elSignIn_submit"]').click()
navegador.find_element(By.NAME, 'q').send_keys("Myria Pedron")
navegador.find_element(By.XPATH, '//*[@id="elSearch"]/form/button').click()