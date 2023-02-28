from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, sys, keyboard,string
import random

print("Press X and Z at the same time to close everything. Press S to make a new instance of everything")

def attemptClick(xPath):
    try:
        element = driver.find_element(By.XPATH,xPath)
    except:
        attemptClick(xPath)
    else:
        element.click()

def signIn(target,base,firstTime,postSite,firstLog):

    driver.get(base)
    if firstLog:
        for i in ["/html/body/div[3]/div/header/div/div[3]/div[3]/button","/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div/div[1]/select", "/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div/div[1]/select/option[13]","/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div/div[2]/select","/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div/div[2]/select/option[8]","/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div/div[3]/select","/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div/div[3]/select","/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div/div[3]/select/option[28]",]:
            attemptClick(i)
        if firstTime:
            element = driver.find_element(By.XPATH,"/html/body/div[8]/div[2]/div/div[1]/div/div[2]/div/button[2]")
            element.click()
        element = driver.find_element(By.XPATH,"/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[2]/label/div/input")
        element.send_keys(target)
        element = driver.find_element(By.XPATH,"/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[3]/label/div/input")
        element.send_keys("FuckyouQuizlet1!")


        element = driver.find_element(By.XPATH,"/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/button")
        while(element.get_attribute('disabled')):
            pass
        element.click()
        while(driver.current_url != postSite):
            pass
        element = driver.find_element(By.XPATH,"/html/body/div[3]/main/div/section[1]/section[1]/div/div[3]/div/div/button/span")
        element.click()
    else:
        element = driver.find_element(By.XPATH,"/html/body/div[3]/div/header/div/div[3]/div[2]/button/span")
        element.click()
        element = driver.find_element(By.XPATH,"/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div/label[1]/div/input")
        element.send_keys(target)
        element = driver.find_element(By.XPATH,"/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div/label[2]/div[1]/input")
        element.send_keys("FuckyouQuizlet1!")
        element = driver.find_element(By.XPATH,"/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/button")
        element.click()



driver = webdriver.Chrome("window-size=1200x600")
driver.get("https://www.fakemail.net/")
driver2 = webdriver.Chrome("window-size=1200x600")
element = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[1]/span[1]")
email2 = element.text
driver.switch_to.new_window()
driver.get("https://www.minuteinbox.com/")
element = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/p[2]/span")
email1 = element.text
driver.switch_to.new_window()
driver.get("https://quizlet.com/goodbye")
signIn(email1,"https://quizlet.com/goodbye",True,"https://quizlet.com/upgrade?source=signup&redir=https%3A%2F%2Fquizlet.com%2Fgoodbye",True)
driver.switch_to.new_window()
driver.get("https://www.minuteinbox.com/")
driver.refresh()
driver.refresh()
driver.get("https://www.minuteinbox.com/window/id/2")
temptext = "Confirm your email"
driver.switch_to.frame("iframeMail")
element = driver.find_element(By.XPATH,"/html/body/table/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/a")
element.click()

driver.switch_to.new_window()
driver.get("https://quizlet.com/refer-a-friend")
element = driver.find_element(By.XPATH,"/html/body/div[3]/main/div/div/div[2]/div/div[2]/div[1]/label/input")
refLink = element.get_property("value")
print(refLink)
driver.delete_all_cookies()
driver.refresh()
signIn(email2,refLink,False,"https://quizlet.com/upgrade?source=signup&redir=%2F",True)
driver.switch_to.new_window()
driver.get("https://www.fakemail.net/")
driver.refresh()
driver.refresh()
driver.get("https://www.fakemail.net/window/id/2")
driver.switch_to.frame("iframeMail")
element = driver.find_element(By.XPATH,"/html/body/table/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/a")
element.click()
print("reached here")
driver.switch_to.new_window()
driver.get("https://quizlet.com/goodbye")
driver.delete_all_cookies()
driver.refresh()
signIn(email1,"https://quizlet.com/goodbye",False,"https://quizlet.com/upgrade?source=signup&redir=https%3A%2F%2Fquizlet.com%2Fgoodbye",False)
while True:
    if (keyboard.is_pressed("x") and keyboard.is_pressed("z")):
        print('STOP THE CODE')
        sys.exit(0)
"""
driver.delete_all_cookies()
driver.refresh()
signIn(email1,"https://quizlet.com/goodbye",True,"https://quizlet.com/upgrade?source=signup&redir=https%3A%2F%2Fquizlet.com%2Fgoodbye",False)
driver.get("hhttps://www.fakemail.net/")
while True:
    if (keyboard.is_pressed("x") and keyboard.is_pressed("z")):
        print('STOP THE CODE')
        sys.exit(0)"""
"""
element = driver.find_element(By.XPATH,"/html/body/div[1]/div[5]/div/div[1]/table/tbody/tr[3]/td[1]")
while True:
    if (keyboard.is_pressed("x") and keyboard.is_pressed("z")):
        print('STOP THE CODE')
        sys.exit(0)


driver.get("https://quizlet.com/explanations/textbook-solutions/calculus-early-transcendentals-9th-edition-9781337613927")
driver.refresh()
"""
