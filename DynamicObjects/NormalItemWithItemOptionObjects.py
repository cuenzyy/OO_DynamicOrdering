import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class NormalItemOption:
    def __init__(self, driver):
        self.driver = driver

    # LOGIN
    Login = (By.XPATH, "//ul[@id='navbar-header'][2]/li[2]")
    email = (By.XPATH, "//form[@id='login-form']/div[2]/input")
    password = (By.XPATH, "//form[@id='login-form']/div[3]/input")
    LoginBtn = (By.XPATH, "//button[@id='login']")
    # LOGIN

    ScrollDown = "window.scrollBy(0, 2700);"

    # Select Normal Item w Item Option
    ItemSelected01 = (By.XPATH, "//div[@id='menu-items']/div[5]/div[1]/ul/li[12]")

    # Select Item Option
    ItemOption01 = (By.XPATH, "(//div[@class='item-option-radio item-option-radio-menu row'])[13]/div[2]")

    # Add Item Button
    AddItem01 = (By.XPATH, "(//input[@id='209004'])[1]")

    # Process Order
    ViewCart = (By.XPATH, "//li[@id='show_cart']")
    GoCheckout = (By.XPATH, "//button[@id='bt-checkout']")
    GoPay = (By.XPATH, "//input[@id='pay']")

    # Logout Process
    ProfileBtn = (By.XPATH, "//ul[@id='navbar-header'][2]/li[3]")
    LogoutBtn = (By.XPATH, "//ul[@id='navbar-header'][2]/li[3]/div/div[2]/ul/li[2]/a")

    def mtLogin(self):
        waitElement = WebDriverWait(self.driver, 10)
        Login = waitElement.until(ec.presence_of_element_located(NormalItemOption.Login))
        return Login

    def mtemail(self):
        waitElement = WebDriverWait(self.driver, 10)
        email = waitElement.until(ec.presence_of_element_located(NormalItemOption.email))
        return email

    def mtpassword(self):
        waitElement = WebDriverWait(self.driver, 10)
        password = waitElement.until(ec.presence_of_element_located(NormalItemOption.password))
        return password

    def mtLoginBtn(self):
        waitElement = WebDriverWait(self.driver, 10)
        LoginBtn = waitElement.until(ec.presence_of_element_located(NormalItemOption.LoginBtn))
        return LoginBtn

    def mtScrollDown(self):
        return self.driver.execute_script(NormalItemOption.ScrollDown)

    def mtItemSelected01(self):
        waitElement = WebDriverWait(self.driver, 10)
        ItemSelected01 = waitElement.until(ec.presence_of_element_located(NormalItemOption.ItemSelected01))
        return ItemSelected01

    def mtItemOption01(self):
        waitElement = WebDriverWait(self.driver, 10)
        ItemOption01 = waitElement.until(ec.presence_of_element_located(NormalItemOption.ItemOption01))
        return ItemOption01

    def mtAddItem01(self):
        waitElement = WebDriverWait(self.driver, 10)
        AddItem01 = waitElement.until(ec.presence_of_element_located(NormalItemOption.AddItem01))
        return AddItem01

    def mtViewCart(self):
        waitElement = WebDriverWait(self.driver, 10)
        ViewCart = waitElement.until(ec.presence_of_element_located(NormalItemOption.ViewCart))
        return ViewCart

    def mtGoCheckout(self):
        waitElement = WebDriverWait(self.driver, 10)
        GoCheckout = waitElement.until(ec.presence_of_element_located(NormalItemOption.GoCheckout))
        return GoCheckout

    def mtGoPay(self):
        waitElement = WebDriverWait(self.driver, 10)
        GoPay = waitElement.until(ec.presence_of_element_located(NormalItemOption.GoPay))
        return GoPay

    def mtProfileBtn(self):
        waitElement = WebDriverWait(self.driver, 10)
        ProfileBtn = waitElement.until(ec.presence_of_element_located(NormalItemOption.ProfileBtn))
        return ProfileBtn

    def mtLogoutBtn(self):
        waitElement = WebDriverWait(self.driver, 10)
        LogoutBtn = waitElement.until(ec.presence_of_element_located(NormalItemOption.LogoutBtn))
        return LogoutBtn

    def generate_SS(self):
        timestamp = time.strftime("%Y%m%d%H%M%S")
        SS = self.driver.get_screenshot_as_file(timestamp + ".png")
        return SS