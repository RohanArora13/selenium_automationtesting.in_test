import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_utilities import getChromeDriver
from selenium.common.exceptions import NoSuchElementException        
import requests

"""
created by Rohan Arora @copyright owner
contact email - contact@rohans.in

"""

apicall = requests.get("https://random.justyy.workers.dev/api/random/?cached&n=12")
response = apicall.json()

apicall = requests.get("https://random.justyy.workers.dev/api/random/?cached&n=6&x=3")
name = apicall.json()

emailid = name+'@exdonts.com'
password_txt = response
print(password_txt)

with open("passwords.txt", 'a') as f:
    f.write("\n\npassword = "+password_txt)
    f.write("\nemail = "+emailid)
    f.close()


driver = webdriver.Chrome(executable_path=getChromeDriver())
#driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(3)


def register_account():

    my_account_menu_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-50"]/a').click()

    email_field = driver.find_element(By.ID,'reg_email')
    email_field.send_keys(emailid) # temprary email made using instaAddrs
    password_field = driver.find_element(By.ID,'reg_password')
    password_field.send_keys(password_txt)
    register_btn = driver.find_element(By.XPATH,'//*[@id="customer_login"]/div[2]/form/p[3]/input[3]').click()
    time.sleep(3)
    password_field.send_keys('..')
    try:
        password_message = driver.find_element(By.CLASS_NAME,"woocommerce-password-strength bad") #woocommerce-password-strength bad #/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[2]/div
        print ("password to weak!, please change password")

    except NoSuchElementException:
        register_btn = driver.find_element(By.XPATH,'//*[@id="customer_login"]/div[2]/form/p[3]/input[3]').click()
        
        #register_work_btn = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID, "reg_password")) )


        # check if there is an error after registeration click
        try:

            check_error = driver.find_element(By.CLASS_NAME,"woocommerce-error") #woocommerce-password-strength bad #/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[2]/div
            print ("account registeration error (probably email already in use)")

        except NoSuchElementException:

            try:
                driver.find_element(By.CLASS_NAME,"woocommerce-MyAccount-content")
                print ("account registered successfully")

            except:
                print ("account registered failed")


def login():
    driver.execute_script("window.open();")
    window_after = driver.window_handles[1]
    driver.close()
    driver.switch_to.window(window_after) 
    driver.get("http://practice.automationtesting.in/") 
    my_account_menu_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-50"]/a').click()
    username = driver.find_element(By.ID,'username')
    username.send_keys(emailid)
    password = driver.find_element(By.ID,'password')
    password.send_keys(password_txt)
    login_btn = driver.find_element(By.XPATH,'//*[@id="customer_login"]/div[1]/form/p[3]/input[3]').click()
    logout_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-36"]/div/div[1]/nav/ul/li[6]/a')) )


register_account()
login()
