import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class NormalItemObjectClass:
    def __init__(self, driver):
        self.driver = driver
    Login = (By.XPATH, "//ul[@id='navbar-header'][2]/li[2]")
    email = (By.XPATH, "//form[@id='login-form']/div[2]/input")
    password = (By.XPATH, "//form[@id='login-form']/div[3]/input")
    LoginBtn = (By.XPATH, "//button[@id='login']")
    ScrollDown = "window.scrollBy(0, 2200);"
    ItemSelected01 = (By.XPATH, "//div[@id='menu-items']/div[5]/div[1]/ul/li[1]")
    AddItem01 = (By.XPATH, "(//input[@id='209002'])[1]")
    ViewCart = (By.XPATH, "//li[@id='show_cart']")
    GoCheckout = (By.XPATH, "//button[@id='bt-checkout']")
    GoPay = (By.XPATH, "//input[@id='pay']")
    ProfileBtn = (By.XPATH, "//ul[@id='navbar-header'][2]/li[3]")
    LogoutBtn = (By.XPATH, "//ul[@id='navbar-header'][2]/li[3]/div/div[2]/ul/li[2]/a")

    def mtLogin(self):
        waitElement = WebDriverWait(self.driver, 10)
        Login = waitElement.until(ec.presence_of_element_located(NormalItemObjectClass.Login))
        return Login

    def mtemail(self):
        waitElement = WebDriverWait(self.driver, 10)
        email = waitElement.until(ec.presence_of_element_located(NormalItemObjectClass.email))
        return email

    def mtpassword(self):
        waitElement = WebDriverWait(self.driver, 10)
        password = waitElement.until(ec.presence_of_element_located(NormalItemObjectClass.password))
        return password

    def mtLoginBtn(self):
        waitElement = WebDriverWait(self.driver, 10)
        LoginBtn = waitElement.until(ec.presence_of_element_located(NormalItemObjectClass.LoginBtn))
        return LoginBtn

    def mtScrollDown(self):
        return self.driver.execute_script(NormalItemObjectClass.ScrollDown)

    def mtItemSelected01(self):
        waitElement = WebDriverWait(self.driver, 10)
        ItemSelected01 = waitElement.until(ec.presence_of_element_located(NormalItemObjectClass.ItemSelected01))
        return ItemSelected01

    def mtAddItem01(self):
        waitElement = WebDriverWait(self.driver, 10)
        AddItem01 = waitElement.until(ec.presence_of_element_located(NormalItemObjectClass.AddItem01))
        return AddItem01

    def mtViewCart(self):
        waitElement = WebDriverWait(self.driver, 10)
        ViewCart = waitElement.until(ec.presence_of_element_located(NormalItemObjectClass.ViewCart))
        return ViewCart

    def mtGoCheckout(self):
        waitElement = WebDriverWait(self.driver, 10)
        GoCheckout = waitElement.until(ec.presence_of_element_located(NormalItemObjectClass.GoCheckout))
        return GoCheckout

    def mtGoPay(self):
        waitElement = WebDriverWait(self.driver, 10)
        GoPay = waitElement.until(ec.presence_of_element_located(NormalItemObjectClass.GoPay))
        return GoPay

    def mtProfileBtn(self):
        waitElement = WebDriverWait(self.driver, 10)
        ProfileBtn = waitElement.until(ec.presence_of_element_located(NormalItemObjectClass.ProfileBtn))
        return ProfileBtn

    def mtLogoutBtn(self):
        waitElement = WebDriverWait(self.driver, 10)
        LogoutBtn = waitElement.until(ec.presence_of_element_located(NormalItemObjectClass.LogoutBtn))
        return LogoutBtn

    def generate_SS(self):
        timestamp = time.strftime("%Y%m%d%H%M%S")
        SS = self.driver.get_screenshot_as_file(timestamp + ".png")
        return SS

    # def clickQuick02(self):
    #     waitElement = WebDriverWait(self.driver, 10)
    #     clickQuick03 = waitElement.until(ec.presence_of_element_located(GFO_Locators.clickQuick01))
    #     return clickQuick03
    # def click_Add(self):
    #     return self.driver.find_element(*CheckoutPage.clickAdd)
    #
    # def click_Checkout(self):
    #     return self.driver.find_element(*CheckoutPage.clickCheckout)

    # self.driver.execute_script("window.scrollBy(0, 1200);")


