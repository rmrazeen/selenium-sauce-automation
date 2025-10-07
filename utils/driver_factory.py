from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver(browser_name="chrome"):
    if browser_name.lower() == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        return driver
    else:
        raise ValueError(f"Browser '{browser_name}' is not supported.")
