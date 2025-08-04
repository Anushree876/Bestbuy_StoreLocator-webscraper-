import csv
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)

driver.get("https://www.bestbuy.com")
time.sleep(3)

us_button=driver.find_element(By.LINK_TEXT,value="United States")
us_button.click()

store_locator=driver.find_element(By.CLASS_NAME,value="store-display-name")
store_locator.click()
store_locator_1=driver.find_element(By.LINK_TEXT,value="Find Another Store")
store_locator_1.click()

try:
    zipcode=driver.find_element(By.CLASS_NAME,value="zip-code-input")
    zipcode.send_keys("10001")
except Exception as e:
    print(f"Error entering the zipcode:{e}")
    sys.exit(1)

try:
    search_btn=driver.find_element(By.CLASS_NAME,value="location-zip-code-form-update-btn")
    search_btn.click()
except Exception as e:
    print(f"Error finding the search button:{e}")
    sys.exit(1)

time.sleep(3)

try:
    detail_links=[a.get_attribute("href") for a in driver.find_elements(By.LINK_TEXT,value="Store Details")]
except Exception as e:
    print("Error finding the store details. ")
    detail_links=[]

try:
    with open('data.csv',mode='w',newline='',encoding='utf-8') as file:
        writer=csv.writer(file)
        writer.writerow(["Store_Name","Address","Contact","Rating","Services"])

        for store in detail_links[:5]:
            store_name="N/A"
            address="N/A"
            contact="N/A"
            rating="N/A"
            services_all = "N/A"

            driver.get(store)
            time.sleep(2)
            try:
                store_name=driver.find_element(By.CSS_SELECTOR,value="h1.Heading.Heading--head").text
                print(store_name)
            except Exception as e:
                store_name="N/A"
                print(store_name)
            try:
                address=driver.find_element(By.CSS_SELECTOR,value="a.Link--underline.ml-2").text.strip()
            except Exception as e:
                address="N/A"
                print(f"{e}")

            try:
                contact=driver.find_element(By.CSS_SELECTOR,value="div span.ml-2.hidden.sm\\:inline").text.strip()
            except Exception as e:
                contact="N/A"
                print(f"contact;{e}")

            try:
                rating=driver.find_element(By.CSS_SELECTOR,value="span.mr-2").text.strip()
            except Exception as e:
                print(f"rating:{e}")
                rating="N/A"

            try:
                services = [service.text.strip() for service in
                            driver.find_elements(By.CSS_SELECTOR, "div.px-3.mb-1\\.5.leading-6.w-full")]
                services_all = ", ".join(services)
            except Exception as e:
                print(f"Services error: {e}")

            writer.writerow([store_name, address, contact, rating, services_all])
            print(f"store={store_name}")
            print(f"address={address}")
            print(f"contact={contact}")
            print(f"rating={rating}")
            print(f"serivces={services_all}")



except Exception as e:
    print(f"Error :{e}")




