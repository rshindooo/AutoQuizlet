

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, sys, keyboard,string
import random
driver = webdriver.Chrome("window-size=1200x600")

driver.get("https://quizlet.com/goodbye")

def email_gen():
    return ( ''.join(random.choice(string.ascii_lowercase) for i in range(10)) )+"@gmail.com"

for i in ["/html/body/div[3]/div/header/div/div[3]/div[3]/button", "/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div/div[1]/select", "/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div/div[1]/select/option[13]", "/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div/div[2]/select","/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div/div[2]/select/option[8]","/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div/div[3]/select","/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div/div[3]/select","/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div/div[3]/select/option[28]",]:
    element = driver.find_element(By.XPATH,i)
    element.click()

element = driver.find_element(By.XPATH,"/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[2]/label/div/input")
element.send_keys(email_gen())
element = driver.find_element(By.XPATH,"/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[3]/label/div/input")
element.send_keys("FuckyouQuizlet1!")
element = driver.find_element(By.XPATH,"/html/body/div[8]/div[2]/div/div[2]/button")
element.click()

element = driver.find_element(By.XPATH,"/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/button")
while(element.get_attribute('disabled')):
       pass
element.click()
driver.switch_to.new_window()
driver.get("https://quizlet.com/explanations/textbook-solutions/calculus-early-transcendentals-9th-edition-9781337613927")
driver.refresh()
while True:
    if (keyboard.is_pressed("x") and keyboard.is_pressed("z")):
        print('STOP THE CODE')
        sys.exit(0)
