from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, sys, keyboard,string
import random

def attemptClick(xPath,whichDriver):
    try:
        element = whichDriver.find_element(By.XPATH,xPath)
    except:
        attemptClick(xPath,whichDriver)
    else:
        element.click()
def signIn(whichDriver,whichEmail,startSite,xOUT,SiteAfterLog,SignUpInstead):
    whichDriver.get(startSite)
    if SignUpInstead:
        for i in ["/html/body/div[3]/div/header/div/div[3]/div[3]/button","/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div/div[1]/select", "/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div/div[1]/select/option[13]","/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div/div[2]/select","/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div/div[2]/select/option[8]","/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div/div[3]/select","/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div/div[3]/select","/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[1]/div/div/div/div[3]/select/option[28]",]:
            attemptClick(i,whichDriver)
        try:
            element = whichDriver.find_element(By.XPATH,"/html/body/div[8]/div[2]/div/div[1]/div/div[2]/div/button[2]")
        except:
            pass
        else:
            element.click()
        element = whichDriver.find_element(By.XPATH,"/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[2]/label/div/input")
        element.send_keys(whichEmail)
        element = whichDriver.find_element(By.XPATH,"/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div[3]/label/div/input")
        element.send_keys("FuckyouQuizlet1!")
        element = whichDriver.find_element(By.XPATH,"/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/button")
        while(element.get_attribute('disabled')):
            pass
        element.click()
        while(whichDriver.current_url != SiteAfterLog):
            pass
        element = whichDriver.find_element(By.XPATH,"/html/body/div[3]/main/div/section[1]/section[1]/div/div[3]/div/div/button/span")
        element.click()
    else:
        element = whichDriver.find_element(By.XPATH,"/html/body/div[3]/div/header/div/div[3]/div[2]/button/span")
        element.click()
        element = whichDriver.find_element(By.XPATH,"/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div/label[1]/div/input")
        element.send_keys(whichEmail)
        element = whichDriver.find_element(By.XPATH,"/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/div/label[2]/div[1]/input")
        element.send_keys("FuckyouQuizlet1!")
        element = whichDriver.find_element(By.XPATH,"/html/body/div[10]/div/div/div[2]/section/div[2]/div/form/button")
        element.click()

driverMAIN = webdriver.Chrome("window-size=1200x600")
driverALT = webdriver.Chrome("window-size=1200x600")
driverALT.get("https://www.minuteinbox.com/")
driverMAIN.get("https://www.fakemail.net/")
targetElement = driverMAIN.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div[1]/span[1]")
emailMAIN = targetElement.text
targetElement = driverALT.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/p[2]/span")
emailALT = targetElement.text
for i in [driverMAIN,driverALT]:
    i.switch_to.new_window()
    i.get("https://quizlet.com/goodbye")
print("Phase 1 complete: Both emails recognized as "+emailALT+" and "+emailMAIN)
signIn(driverMAIN,emailMAIN,"https://quizlet.com/goodbye",True,"https://quizlet.com/upgrade?source=signup&redir=https%3A%2F%2Fquizlet.com%2Fgoodbye",True)
driverMAIN.switch_to.new_window()
driverMAIN.get("https://quizlet.com/refer-a-friend")
targetElement = driverMAIN.find_element(By.XPATH,"/html/body/div[3]/main/div/div/div[2]/div/div[2]/div[1]/label/input")
refLink = targetElement.get_property("value")
print(refLink+" recognized as ref link.")
driverALT.get(refLink)
signIn(driverALT,emailALT,refLink,False,"https://quizlet.com/upgrade?source=signup&redir=%2F",True)
print("Phase 2 complete: Both emails init, one with ref link")
driverMAIN.switch_to.new_window()
driverMAIN.get("https://www.fakemail.net/window/id/2")
driverMAIN.switch_to.frame("iframeMail")
targetElement = driverMAIN.find_element(By.XPATH,"/html/body/table/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/a")
targetElement.click()
driverALT.switch_to.new_window()
driverALT.get("https://www.minuteinbox.com/")
driverALT.refresh()
driverALT.get("https://www.minuteinbox.com/window/id/2")
driverALT.switch_to.frame("iframeMail")
targetElement = driverALT.find_element(By.XPATH,"/html/body/table/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td/a")
targetElement.click()
driverMAIN.refresh()
driverMAIN.switch_to.new_window()
driverMAIN.get("https://quizlet.com/explanations/textbook-solutions/calculus-early-transcendentals-9th-edition-9781337613927")
driverMAIN.refresh()
driverMAIN.refresh()
while True:
    if (keyboard.is_pressed("x") and keyboard.is_pressed("z")):
        print('STOP THE CODE')
        sys.exit(0)
