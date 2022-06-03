import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium_utilities import getChromeDriver


"""
created by Rohan Arora @copyright owner
contact email - contact@rohans.in

"""

driver = webdriver.Chrome(executable_path=getChromeDriver())
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)
my_account_menu_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-50"]/a').click()

email = "rihit5@exdonuts.com"
password_txt = "RohanTest@1314@!"

#SHOP product page display
username = driver.find_element(By.ID,'username')
username.send_keys(email)
password = driver.find_element(By.XPATH,'//*[@id="password"]')
password.send_keys(password_txt)
login_btn = driver.find_element(By.XPATH,'//*[@id="customer_login"]/div[1]/form/p[3]/input[3]').click()
shop_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-40"]/a').click()

#scroll down to find the desired element
driver.execute_script("window.scrollBy(0, 600);")
html_5forms_btn = driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[3]/a[1]/h3').click()
html_5forms_check = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "product_title.entry-title"), "HTML5 Forms"))

def shop_product_check():
    #SHOP number of products in category
    driver.execute_script("window.open();")#opening a new tab
    window_after = driver.window_handles[1]#creating a variable where we specify the path to the second tab (window_handles[1]) ; here it will be 1, since the countdown starts from 0
    driver.switch_to.window(window_after) #switch the scope of the driver to a new tab, now the driver will look for further elements already there
    driver.get("http://practice.automationtesting.in/")

    my_account_menu_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-50"]/a').click()
    shop_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-40"]/a').click()
    #the fields below are not required because the account is authorized, but in case there is no authorization, let it be
    #username = driver.find_element(By.ID,'username')
    #username.send_keys('rihit5@exdonuts.com')
    #password = driver.find_element(By.ID,'password')
    #password.send_keys('Rohantest123@!!')
    #login_btn = driver.find_element(By.XPATH,'//*[@id="customer_login"]/div[1]/form/p[3]/input[3]').click()
    html_category_btn = driver.find_element(By.XPATH,'//*[@id="woocommerce_product_categories-2"]/ul/li[2]/a').click()

    check_amount_html = driver.find_elements(By.CSS_SELECTOR,'.products.masonry-done > li')
    assert len(check_amount_html) == 3


def shop_sorting():
    #shop sorting goods
    driver.execute_script("window.open();")#opening a new tab
    window_after = driver.window_handles[2]#creating a variable where we specify the path to the second tab (window_handles[1]) ; here it will be 1, since the countdown starts from 0
    driver.switch_to.window(window_after) #switch the scope of the driver to a new tab, now the driver will look for further elements already there
    driver.get("http://practice.automationtesting.in/")

    shop_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-40"]/a').click()
    selector = driver.find_element(By.CLASS_NAME,'orderby').click()
    check_selector = driver.find_element(By.CSS_SELECTOR,"[value='menu_order']")
    check_attribute = check_selector.get_attribute('selected')
    assert check_attribute is not None

    element = driver.find_element(By.CLASS_NAME,"orderby") #"element" is just a variable name, you can specify something else
    select = Select(element) #The select after the "=" must be capitalized as it is capitalized in import
    select.select_by_value("price") #looking for an element with the text "Sales" ; in this and the previous method, you do not need to add .click()

    selector = driver.find_element(By.CLASS_NAME,'orderby').click()
    check_selector = driver.find_element(By.CSS_SELECTOR,"[value='price']")
    check_attribute = check_selector.get_attribute('selected')
    assert check_attribute is not None


def check_discount_items(driver):
    #SHOP Display discount item
    driver.execute_script("window.open();")#opening a new tab
    window_after = driver.window_handles[3]#creating a variable where we specify the path to the second tab (window_handles[1]) ; here it will be 1, since the countdown starts from 0
    driver.switch_to.window(window_after) #switch the scope of the driver to a new tab, now the driver will look for further elements already there
    driver.get("http://practice.automationtesting.in/")

    shop_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-40"]/a').click()
    android_book = driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[1]/a[1]/h3')
    #scroll to desired argument in our case android_book
    driver.execute_script("return arguments[0].scrollIntoView(true);", android_book)
    android_book.click()

    old_price = driver.find_element(By.XPATH,'//*[@id="product-169"]/div[2]/div[1]/p/del/span')
    assert old_price.text == '₹600.00'
    new_price = driver.find_element(By.XPATH,'//*[@id="product-169"]/div[2]/div[1]/p/ins/span')
    assert new_price.text == '₹450.00'

    image_click = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="product-169"]/div[1]/a/img')) )
    image_click.click()
    close_image = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close')) )
    close_image.click()

    #SHOP check the price in the cart.
    driver.execute_script("window.open();")#opening a new tab
    window_after = driver.window_handles[4]#creating a variable where we specify the path to the second tab (window_handles[1]) ; here it will be 1, since the countdown starts from 0
    driver.switch_to.window(window_after) #switch the scope of the driver to a new tab, now the driver will look for further elements already there
    driver = webdriver.Chrome(executable_path=getChromeDriver())
    driver.maximize_window()
    driver.get("http://practice.automationtesting.in/")

    shop_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-40"]/a').click()
    #html_wd = driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[4]/a[2]')
    #driver.execute_script("return arguments[0].scrollIntoView(true);", html_wd)
    html_wd_click = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/ul/li[4]/a[2]')) )

    html_wd = driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[4]/a[2]').click()

    time.sleep(7)

    items = driver.find_element(By.CLASS_NAME,'cartcontents')
    assert items.text == '1 Item'
    amount = driver.find_element(By.XPATH,'//*[@id="wpmenucartli"]/a/span[2]')
    assert amount.text == '₹180.00'
    amount.click()


    subtotal = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH,'//*[@id="page-34"]/div/div[1]/div/div/table/tbody/tr[1]/td/span'), "180.00"))
    total = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.XPATH,'//*[@id="page-34"]/div/div[1]/div/div/table/tbody/tr[3]/td/strong/span'), "183.60"))


def add_to_cart():

    #SHOP work in the cart
    driver.execute_script("window.open();")#opening a new tab
    window_after = driver.window_handles[1]#creating a variable where we specify the path to the second tab (window_handles[1]) ; here it will be 1, since the countdown starts from 0
    driver.switch_to.window(window_after) #switch the scope of the driver to a new tab, now the driver will look for further elements already there
    driver.get("http://practice.automationtesting.in/")


    shop_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-40"]/a').click()
    driver.execute_script("window.scrollBy(0, 300);")
    html_wd = driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[4]/a[2]').click()
    html5_webd = driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[4]/a[2]').click()
    time.sleep(3)

    js_data_structures = driver.find_element(By.XPATH,'//*[@id="content"]/ul/li[5]/a[2]').click()
    items_btn = driver.find_element(By.XPATH,'//*[@id="wpmenucartli"]/a/span[2]').click()

    time.sleep(2)
    delete_book = driver.find_element(By.XPATH,'//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[1]/a').click()

    und_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-34"]/div/div[1]/div[1]/a')) )
    und_btn.click()


    quantity_js_field = driver.find_element(By.XPATH,'//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input')
    #clear the field
    quantity_js_field.clear()
    quantity_js_field.send_keys(3)
    update_basket_btn = driver.find_element(By.XPATH,'//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[3]/td/input[1]').click()

    quantity_js_field = driver.find_element(By.XPATH,'//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input')
    amount_of_book = quantity_js_field.get_attribute('value')
    assert amount_of_book == '3'

    time.sleep(5)
    apply_coupon = WebDriverWait(driver, 20,).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.coupon > .button')) )
    apply_coupon.click()

    #apply_coupon_btn = driver.find_element(By.CSS_SELECTOR,'.coupon > .button').click()
    time.sleep(3)
    please_enter_coupon_msg = driver.find_element(By.XPATH,'//*[@id="page-34"]/div/div[1]/ul/li')
    #please_enter_coupon_msg = driver.find_element(By.CSS_SELECTOR,'.woocommerce-error > li')

    assert please_enter_coupon_msg.text == 'Please enter a coupon code.'

    #SHOP purchase of goods

def check_checkout_details():

    pesonal_data = {
        'billing_first_name' : 'Rohan',
        'billing_last_name' : 'Test',
        'billing_email' : 'rihit5@exdonuts.com',
        'billing_phone' : '999888777',
        'billing_address_1' : 'Lokhandwala',
        'billing_city' : 'Mumbai',
        'billing_postcode' : '400101'
    }

    print("Filling billing Info")
    driver.execute_script("window.open();")#opening a new tab
    window_after = driver.window_handles[2]#creating a variable where we specify the path to the second tab (window_handles[1]) ; here it will be 1, since the countdown starts from 0
    driver.switch_to.window(window_after) #switch the scope of the driver to a new tab, now the driver will look for further elements already there
    driver.get("http://practice.automationtesting.in/")

    driver.execute_script("window.scrollBy(0, 300);")
    shop_btn = driver.find_element(By.XPATH,'//*[@id="menu-item-40"]/a').click()
    basket = driver.find_element(By.CLASS_NAME,'wpmenucart-contents').click()
    proceed_to_checkout = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="page-34"]/div/div[1]/div/div/div/a')) )
    proceed_to_checkout.click()

    time.sleep(5)
    for field,data in pesonal_data.items():
        print("entering field ="+field)
        #send_data = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.ID, field)))
        send_data = driver.find_element(By.ID,field)

        # check if data is laready entered
        try:
            already_data = send_data.get_attribute("value")
            if not (already_data):
                print(data)
                send_data.send_keys(data)
        except:
            print(data)
            send_data.send_keys(data)


    #select2-chosen-2

    country_field = driver.find_element(By.ID,'select2-chosen-1').click()
    country_enter_field = driver.find_element(By.ID,'s2id_autogen1_search')
    country_enter_field.send_keys('India')
    country_enter_ = driver.find_element(By.XPATH,'//*[@id="select2-results-1"]/li[2]').click()
    #select2-result-label-2287
    # country_enter_field.send_keys(Keys.ENTER)

    state_field = driver.find_element(By.ID,'select2-chosen-2').click()
    state_field_enter = driver.find_element(By.ID,'s2id_autogen2_search')
    state_field_enter.send_keys('Maharashtra')
    state_field_enter.send_keys(Keys.ENTER)



    #russia = driver.find_element(By.CSS_SELECTOR,'[value = "RU"]').click()
    #country_enter_field.send_keys(Keys.ENTER)
    #russia_choose =  driver.find_element(By.ID,'select2-results-1').click()
    time.sleep(5)
    driver.execute_script("window.scrollBy(0, 600);")

    check_payments_btn = driver.find_element(By.ID,'payment_method_cheque')

    try:
        checked = check_payments_btn.get_attribute("checked")
        if(checked == "checked"):
            pass
    # error if attribute not found
    except:
        check_payments_btn.click()

    place_ord_btn = driver.find_element(By.ID,'place_order')
    place_ord_btn.click()

    time.sleep(7)
    end_of_purchase = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

    check_payments_text = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-35"]/div/div[1]/table/tfoot/tr[3]/td'),"Check Payments"))

    print("order placed")
    time.sleep(3)


# different checks


shop_product_check()
shop_sorting()
check_discount_items(driver)
add_to_cart()
check_checkout_details()





