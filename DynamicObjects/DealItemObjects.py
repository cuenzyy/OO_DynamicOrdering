import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class DealObjectClass:
    def __init__(self, driver):
        self.driver = driver

    # LOGIN
    Login = (By.XPATH, "//ul[@id='navbar-header'][2]/li[2]")
    email = (By.XPATH, "//form[@id='login-form']/div[2]/input")
    password = (By.XPATH, "//form[@id='login-form']/div[3]/input")
    LoginBtn = (By.XPATH, "//button[@id='login']")
    # LOGIN

    ScrollDown = "window.scrollBy(0, 1500);"

    # Select Deal from Menu
    DealMenuSelect01 = (By.XPATH, "//div[@id='menu-items']/div[4]/div[1]/ul/li[6]")

    # Selection 1
    DealSelection01 = (By.XPATH, "//div[@id='deal-modal-body-main-DEAL07-215317']/p[1]")
    DealSelected01 = (By.XPATH, "//div[@id='deal-modal-body-selection-list-DEAL07-215317-1']/ul/li[1]")
    DealSelectedBtn01 = (By.XPATH, "//div[@class='item-add-buttons']/div[2]/div[@id='deal-modal-footer-next-DEAL07-215317']/button")

    # Selection 2
    DealSelection02 = (By.XPATH, "//div[@id='deal-modal-body-main-DEAL07-215317']/p[2]")
    DealSelected02 = (By.XPATH, "//div[@id='deal-modal-body-selection-list-DEAL07-215317-2']/ul/li[1]")
    # DealSelectedBtn02 = (By.XPATH, "//div[@class='item-add-buttons']/div[2]/div[@id='deal-modal-footer-next-DEAL07-215317']/button")

    # Final Add After selection of deals
    DealMenuSelectBtn01 = (By.XPATH, "//div[@id='deal-modal-footer-add-DEAL07-215317']/button")

    # Process Order
    ViewCart = (By.XPATH, "//li[@id='show_cart']")
    GoCheckout = (By.XPATH, "//button[@id='bt-checkout']")
    GoPay = (By.XPATH, "//input[@id='pay']")

    # Logout Process
    ProfileBtn = (By.XPATH, "//ul[@id='navbar-header'][2]/li[3]")
    LogoutBtn = (By.XPATH, "//ul[@id='navbar-header'][2]/li[3]/div/div[2]/ul/li[2]/a")

    # LOGIN
    def mtLogin(self):
        waitElement = WebDriverWait(self.driver, 10)
        Login = waitElement.until(ec.presence_of_element_located(DealObjectClass.Login))
        return Login

    def mtemail(self):
        waitElement = WebDriverWait(self.driver, 10)
        email = waitElement.until(ec.presence_of_element_located(DealObjectClass.email))
        return email

    def mtpassword(self):
        waitElement = WebDriverWait(self.driver, 10)
        password = waitElement.until(ec.presence_of_element_located(DealObjectClass.password))
        return password

    def mtLoginBtn(self):
        waitElement = WebDriverWait(self.driver, 10)
        LoginBtn = waitElement.until(ec.presence_of_element_located(DealObjectClass.LoginBtn))
        return LoginBtn

    # LOGIN

    def mtScrollDown(self):
        return self.driver.execute_script(DealObjectClass.ScrollDown)

    # SELECT DEAL ITEM

    def mtDealMenuSelect01(self):
        waitElement = WebDriverWait(self.driver, 10)
        DealMenuSelect01 = waitElement.until(ec.presence_of_element_located(DealObjectClass.DealMenuSelect01))
        return DealMenuSelect01

    # SELECT DEAL ITEM

    # DEAL SELECTION PROCESS
    # 1
    def mtDealSelection01(self):
        waitElement = WebDriverWait(self.driver, 10)
        DealSelection01 = waitElement.until(ec.presence_of_element_located(DealObjectClass.DealSelection01))
        return DealSelection01

    def mtDealSelected01(self):
        waitElement = WebDriverWait(self.driver, 10)
        DealSelected01 = waitElement.until(ec.presence_of_element_located(DealObjectClass.DealSelected01))
        return DealSelected01

    def mtDealSelectedBtn01(self):
        waitElement = WebDriverWait(self.driver, 10)
        DealSelectedBtn01 = waitElement.until(ec.presence_of_element_located(DealObjectClass.DealSelectedBtn01))
        return DealSelectedBtn01

    # 1
    # 2
    def mtDealSelection02(self):
        waitElement = WebDriverWait(self.driver, 10)
        DealSelection02 = waitElement.until(ec.presence_of_element_located(DealObjectClass.DealSelection02))
        return DealSelection02

    def mtDealSelected02(self):
        waitElement = WebDriverWait(self.driver, 10)
        DealSelected02 = waitElement.until(ec.presence_of_element_located(DealObjectClass.DealSelected02))
        return DealSelected02

    # def mtDealSelectedBtn02(self):
    #     waitElement = WebDriverWait(self.driver, 10)
    #     DealSelectedBtn02 = waitElement.until(ec.presence_of_element_located(DealObjectClass.DealSelectedBtn02))
    #     return DealSelectedBtn02
    # 2

    # ADD DEAL
    def mtDealMenuSelectBtn01(self):
        waitElement = WebDriverWait(self.driver, 10)
        DealMenuSelectBtn01 = waitElement.until(ec.presence_of_element_located(DealObjectClass.DealMenuSelectBtn01))
        return DealMenuSelectBtn01

    # DEAL SELECTION PROCESS

    # PROCESS TO PAY ORDER

    # METHODS
    def mtViewCart(self):
        waitElement = WebDriverWait(self.driver, 10)
        ViewCart = waitElement.until(ec.presence_of_element_located(DealObjectClass.ViewCart))
        return ViewCart

    def mtGoCheckout(self):
        waitElement = WebDriverWait(self.driver, 10)
        GoCheckout = waitElement.until(ec.presence_of_element_located(DealObjectClass.GoCheckout))
        return GoCheckout

    def mtGoPay(self):
        waitElement = WebDriverWait(self.driver, 10)
        GoPay = waitElement.until(ec.presence_of_element_located(DealObjectClass.GoPay))
        return GoPay

    # PROCESS TO PAY ORDER

    # PROCESS TO LOGOUT

    def mtProfileBtn(self):
        waitElement = WebDriverWait(self.driver, 10)
        ProfileBtn = waitElement.until(ec.presence_of_element_located(DealObjectClass.ProfileBtn))
        return ProfileBtn

    def mtLogoutBtn(self):
        waitElement = WebDriverWait(self.driver, 10)
        LogoutBtn = waitElement.until(ec.presence_of_element_located(DealObjectClass.LogoutBtn))
        return LogoutBtn

    # PROCESS TO LOGOUT

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


