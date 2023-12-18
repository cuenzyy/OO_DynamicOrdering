from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--incognito")

# accessing google profile
options.add_argument('--profile-directory=Profile 1')
options.add_argument('--user-data-dir=C:\\Users\\vince\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1')
driver = uc.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe", options=options)

driver.maximize_window()
driver.get("https://orderonline.dev.dsoftonline.com.au/vincent-store-01/")

time.sleep(5)

ClickItem01 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@id='menu-items']/div[5]/div[1]/ul/li[12]"))
)
ClickItem01.click()
time.sleep(3)

ClickItem02 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "(//div[@class='item-option-radio item-option-radio-menu row'])[13]/div[2]"))
)
ClickItem02.click()
time.sleep(3)
