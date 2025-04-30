#https://github.com/jacks-somewhere
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--headless=new")

import time
import sys


firstname = 'first name here'
lastname = 'last name here'
email = 'email here' #do NOT include @eagle.fgcu.edu or @fgcu.edu

day = 3 #number of days clicked through

startTime = 9 #starting hour
startMin = '00' #'00' or '30'
startAP = 'pm' #lower case am or pm

endTime = 10 #ending hour 
endMin = '00' #'00' or '30'

noBookRoomList = [113,116] #list of all rooms that should not be booked
room = 110 #lowest room number


driver = webdriver.Chrome(options=chrome_options)
driver.get('https://fgcu.libcal.com/r/new/availability?lid=1191&zone=0&gid=0&capacity=1')
print(driver.title)

time.sleep(2)

for i in range(day): 
    next_element = driver.find_element(By.CSS_SELECTOR, '[class*="chevron-right"]')
    next_element.click()

    time.sleep(1)
            
while True:

    try:
        print(f'Trying room {room} now')
        #selects time and location
        div_element = driver.find_element(By.CSS_SELECTOR, f'[title*="{startTime}:{startMin}pm"][title*="{room}"]')

        if room in noBookRoomList:
            roomError = 10/0
            
        div_element.click()
        
        print('Start Time Button clicked')

        #selects end time
        drop_element = driver.find_element(By.CSS_SELECTOR, f'[title*="{endTime}:{endMin}"]')
        drop_element.click()
        print('Drop Down Button clicked')

        #goes to next page
        submit_element = driver.find_element(By.ID, 'submit_times')
        submit_element.click()
        print('Next Page')

        time.sleep(1)
        
        #enters information
        firstname_input = driver.find_element(By.ID, 'fname')
        firstname_input.send_keys(f'{firstname}')
        print('First name entered')

        lastname_input = driver.find_element(By.ID, 'lname')
        lastname_input.send_keys(f'{lastname}')
        print('Last name entered')

        email_input = driver.find_element(By.ID, 'email')
        email_input.send_keys(f'{email}@eagle.fgcu.edu')
        print('Email entered')

        time.sleep(2)
        
        finalsubmit_element = driver.find_element(By.ID, 'btn-form-submit')
        finalsubmit_element.click()
        print('Submited')
        
        driver.quit()
        sys.exit()

    except Exception as e:
        print(f'error: room {room} not available')

        room += 1 #addes one to the room number intel room is booked

        if room >= 337: #stops program when last room is reached
            driver.quit()
            sys.exit()
    
