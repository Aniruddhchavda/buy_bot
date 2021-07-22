import time
from selenium import webdriver

browser = webdriver.Chrome(r'C:\Users\anich\Desktop\bot\chromedriver')

browser.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442")

buyButton = False


while not buyButton:
    try:
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-disabled")

        print("Button isn't ready")
        time.sleep(1)
        browser.refresh()
    except:
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-primary")

        print("Button was clicked")
        addToCartBtn.click()
        buyButton = True
        try:
            time.sleep(1)
            browser.refresh()
            myElement1 = browser.find_element_by_class_name("cart-label")
            myElement1.click()
            time.sleep(1)
            myElement2 = browser.find_element_by_class_name("btn-primary")
            myElement2.click()
            time.sleep(1)
            myElement3 = browser.find_element_by_class_name("btn-secondary")
            myElement3.click()
        except:
            print("ERROR !");