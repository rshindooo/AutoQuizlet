from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys, keyboard
from selenium.webdriver.support.ui import Select
import unittest
from selenium.webdriver.chrome.options import Options
import pyperclip as pc
def signUp(driverTarget):
    if(driverTarget == driverALT):
        useEmail = emailALT
    else:
        useEmail = emailMAIN
    targetElement = WebDriverWait(driverTarget,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="TopNavigationReactTarget"]/header/div/div[3]/div[3]/button')))
    targetElement.click()
    for i in range(0,3):
        sub_target = ["birth_month","birth_day","birth_year"][i]

        targetElement = Select(driverTarget.find_element(By.NAME,sub_target))
        targetElement.select_by_index([1,1,29][i])
    
    targetElement = driverTarget.find_element(By.NAME,'email')
    targetElement.send_keys(useEmail)
    targetElement = driverTarget.find_element(By.NAME,'password1')
    targetElement.send_keys("FuckyouQuizlet1!")
    targetElement = WebDriverWait(driverTarget,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"[type='submit']")))
    driverTarget.execute_script("arguments[0].disabled = false", targetElement)
    targetElement.click()
    while(driverTarget.current_url == "https://quizlet.com/goodbye"):
        pass
    if(targetElement==driverMAIN):
        targetElement = driverTarget.find_element(By.CSS_SELECTOR,"[aria-label='Continue to free Quizlet']")
        targetElement.click()



#Phase 0: Set up Windows
options = Options()
#ptions.headless = True
options.add_argument('--window-size=1920,1080')
driverMAIN = webdriver.Chrome(options=options)
driverMAIN.get("https://www.minuteinbox.com/") 
driverALT = webdriver.Chrome(options=options)
driverALT.get("https://www.fakemail.net/")

#Phase 1: Grab emails and make first Quizlet acc
emailMAIN = WebDriverWait(driverMAIN,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="email"]'))).text
emailALT = WebDriverWait(driverALT,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="email"]'))).text
for i in [driverMAIN,driverALT]:
    i.switch_to.new_window()
driverMAIN.get("https://quizlet.com/goodbye")
signUp(driverMAIN)
print("Phase 1 complete: Grab emails and make first Quizlet acc")

#Phase 2: Grab referral link, make second Quizlet account with ref link
driverMAIN.get("https://quizlet.com/refer-a-friend")
targetElement = driverMAIN.find_element(By.XPATH,"/html/body/div[3]/main/div/div/div[2]/div/div[2]/div[1]/label/input")
refLink = targetElement.get_property("value")
driverALT.get(refLink)
signUp(driverALT)
print("Phase 2 complete: Grab referral link, make second Quizlet account with ref link")

#Phase 3: Confirm both emails, print outcome
driverALT.get("https://www.fakemail.net/window/id/2")
while "404" in driverALT.title:
    driverALT.refresh()
driverALT.switch_to.frame("iframeMail")
targetElement = driverALT.find_element(By.PARTIAL_LINK_TEXT, "Confirm your email")
targetElement.click()

print("Final phase complete. Your login:")
print(emailMAIN)
print("FuckyouQuizlet1!")
pc.copy(emailMAIN + "FuckyouQuizlet1!")



#Forces code to persist. Maybe not needed for empty version.
while True:
    if (keyboard.is_pressed("x") and keyboard.is_pressed("z")):
        print('STOP THE CODE')
        driverMAIN.quit()
        driverALT.quit()
        sys.exit(0)
