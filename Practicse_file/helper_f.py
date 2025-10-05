# all helper funvtion of e2e test cases
def add_products(driver, names):
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    for product in products:
        pname = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        if pname in names:
            product.find_element(By.TAG_NAME, "button").click()