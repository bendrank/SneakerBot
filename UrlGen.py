# File to create the Base Url
# https://www.adidas.ca/en/gazelle-shoes/BB5478.html?forceSelSize=BB5478_530 Size=4
# What sizes are currently available
# Add to Cart Button


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from config import keys


def UrlGenwithSize(size,model,name):
     # Size for the shoe
     base=530
     mySize=(size-4)*20
     finalSize=base+mySize
     Url="https://www.adidas.ca/en/"+name+"/"+model+".html?forceSelSize="+model+"_"+str(finalSize)
     print(Url)
     return Url

def UrlGenProduct(name,model):
     url="https://www.adidas.ca/en/"+name+"/"+model+".html"
     return url

def CheckStock(myUrl,model):
     try:
          driver.get(myUrl)
          element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "add_to_bag_form___227O2")))
          username = driver.find_element_by_class_name('gl-dropdown__select-element')
          options = username.find_elements_by_tag_name("option")  # get all the options into a list
          optionsList = []
          for option in options:
               optionsList.append(option.get_attribute('innerHTML'))
          for sizes in optionsList:
               if sizes.isdigit():
                    print("Size "+sizes+" for "+model+" is available ")
     finally:
               driver.quit()

def addToCart(myUrl):
          province_init={"AB":"//li[contains(@class,'selectoption selected')]", "ON":"//div[contains(@class,'rbk-delivery-wrapper')]//li[10]", "BC":"//div[contains(@class,'ffSelectWrapper active')]//li[contains(@class,'selectoption on')]", "MB":"//div[contains(@class,'rbk-delivery-wrapper')]//li[4]","NB":"//div[contains(@class,'rbk-delivery-wrapper')]//li[5]","NL":"//div[contains(@class,'rbk-delivery-wrapper')]//li[6]","NT":"//div[contains(@class,'rbk-delivery-wrapper')]//li[7]","NS":"//div[contains(@class,'rbk-delivery-wrapper')]//li[8]","NU":"//div[contains(@class,'rbk-delivery-wrapper')]//li[9]","PE":"//div[contains(@class,'rbk-delivery-wrapper')]//li[11]","QC":"//div[contains(@class,'rbk-delivery-wrapper')]//li[12]","SK":"//div[contains(@class,'rbk-delivery-wrapper')]//li[13]","YT":"//div[contains(@class,'rbk-delivery-wrapper')]//li[14]"}
          province=str(province_init[str(keys['province_code'])])
          driver = webdriver.Chrome()
          driver.get(myUrl)
          driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "btn-bag", " " ))]').click()
          element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "gl-modal__main-content")))
          driver.find_element_by_xpath("//span[contains(text(),'Checkout')]").click()
          dropdown = driver.find_element_by_class_name("ffSelectButton")
          dropdown.click()
          element = WebDriverWait(driver, 20).until(
              EC.element_to_be_clickable((By.XPATH, province)))
          driver.execute_script("arguments[0].click();", element)
          driver.find_element_by_xpath("//div[contains(@class,'checkbox error-client')]//div[contains(@class,'ffCheckboxWrapper')]")
          driver.find_element_by_xpath("//input[@id='dwfrm_delivery_singleshipping_shippingAddress_addressFields_firstName']").send_keys(keys['first_name'])
          driver.find_element_by_xpath("//input[@id='dwfrm_delivery_singleshipping_shippingAddress_addressFields_lastName']").send_keys(keys['last_name'])
          driver.find_element_by_xpath("//input[@id='dwfrm_delivery_singleshipping_shippingAddress_addressFields_address1']").send_keys(keys['street_address'])
          driver.find_element_by_xpath("//input[@id='dwfrm_delivery_singleshipping_shippingAddress_addressFields_city']").send_keys(keys['city'])
          driver.find_element_by_xpath("//input[@id='dwfrm_delivery_singleshipping_shippingAddress_addressFields_zip']").send_keys(keys['zip_code'])
          driver.find_element_by_xpath("//input[@id='dwfrm_delivery_singleshipping_shippingAddress_addressFields_phone']").send_keys(keys['phone_number'])
          driver.find_element_by_xpath("//input[@id='dwfrm_delivery_singleshipping_shippingAddress_email_emailAddress']").send_keys(keys['email'])


if __name__ == '__main__':
     # load chrome
     driver = webdriver.Chrome()
     productUrl=UrlGenProduct(keys['product_name'],keys['product_model'])
     CheckStock(productUrl,keys['product_model'])
     size=int(input("From the size available list select size:"))
     myUrl=str(UrlGenwithSize(size,keys['product_model'],keys['product_name']))
     addToCart(myUrl)




