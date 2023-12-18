import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HHObjectClass:
    def __init__(self, driver):
        self.driver = driver

    # LOGIN
    Login = (By.XPATH, "//ul[@id='navbar-header'][2]/li[2]")
    email = (By.XPATH, "//form[@id='login-form']/div[2]/input")
    password = (By.XPATH, "//form[@id='login-form']/div[3]/input")
    LoginBtn = (By.XPATH, "//button[@id='login']")
    # LOGIN

    ScrollDown = "window.scrollBy(0, 4000);"

    # Select HH in menu

    HHSelect01 = (By.XPATH, "//div[@id='menu-items']/div[7]/div[1]/ul/li[1]")

    # 1st half
    Click1stHalf = (By.XPATH, "//div[@class='hh-pizza-container']/div/p[1]")
    Click1stHalfPizza = (By.XPATH, "//div[@id='hh-first-item-list']/ul/li[1]")
    Finished1stPizza = (By.XPATH, "(//button[@class='btn'][normalize-space()='Next'])[1]")

    # 2nd half
    Click2ndHalf = (By.XPATH, "//div[@class='hh-pizza-container']/div/p[2]")
    Click2ndHalfPizza = (By.XPATH, "//div[@id='hh-second-item-list']/ul/li[2]")
    Finished2ndPizza = (By.XPATH, "(//button[@class='btn'][normalize-space()='Next'])[1]")
    AddItem01 = (By.XPATH, "(//button[@id='add-half-half'])[1]")

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
        Login = waitElement.until(ec.presence_of_element_located(HHObjectClass.Login))
        return Login

    def mtemail(self):
        waitElement = WebDriverWait(self.driver, 10)
        email = waitElement.until(ec.presence_of_element_located(HHObjectClass.email))
        return email

    def mtpassword(self):
        waitElement = WebDriverWait(self.driver, 10)
        password = waitElement.until(ec.presence_of_element_located(HHObjectClass.password))
        return password

    def mtLoginBtn(self):
        waitElement = WebDriverWait(self.driver, 10)
        LoginBtn = waitElement.until(ec.presence_of_element_located(HHObjectClass.LoginBtn))
        return LoginBtn

    # LOGIN

    def mtScrollDown(self):
        return self.driver.execute_script(HHObjectClass.ScrollDown)

    # HH Item Select
    def mtHHSelect01(self):
        waitElement = WebDriverWait(self.driver, 10)
        HHSelect01 = waitElement.until(ec.presence_of_element_located(HHObjectClass.HHSelect01))
        return HHSelect01

    # 1st Half/Half
    def mtClick1stHalf(self):
        waitElement = WebDriverWait(self.driver, 10)
        Click1stHalf = waitElement.until(ec.presence_of_element_located(HHObjectClass.Click1stHalf))
        return Click1stHalf

    def mtClick1stHalfPizza(self):
        waitElement = WebDriverWait(self.driver, 10)
        Click1stHalfPizza = waitElement.until(ec.presence_of_element_located(HHObjectClass.Click1stHalfPizza))
        return Click1stHalfPizza

    def mtFinished1stPizza(self):
        waitElement = WebDriverWait(self.driver, 10)
        Finished1stPizza = waitElement.until(ec.presence_of_element_located(HHObjectClass.Finished1stPizza))
        return Finished1stPizza

    # 2nd Half/Half
    def mtClick2ndHalf(self):
        waitElement = WebDriverWait(self.driver, 10)
        Click2ndHalf = waitElement.until(ec.presence_of_element_located(HHObjectClass.Click2ndHalf))
        return Click2ndHalf

    def mtClick2ndHalfPizza(self):
        waitElement = WebDriverWait(self.driver, 10)
        Click2ndHalfPizza = waitElement.until(ec.presence_of_element_located(HHObjectClass.Click2ndHalfPizza))
        return Click2ndHalfPizza

    def mtFinished2ndPizza(self):
        waitElement = WebDriverWait(self.driver, 10)
        Finished2ndPizza = waitElement.until(ec.presence_of_element_located(HHObjectClass.Finished2ndPizza))
        return Finished2ndPizza

    def mtAddItem01(self):
        waitElement = WebDriverWait(self.driver, 10)
        AddItem01 = waitElement.until(ec.presence_of_element_located(HHObjectClass.AddItem01))
        return AddItem01

    # Process Order

    def mtViewCart(self):
        waitElement = WebDriverWait(self.driver, 10)
        ViewCart = waitElement.until(ec.presence_of_element_located(HHObjectClass.ViewCart))
        return ViewCart

    def mtGoCheckout(self):
        waitElement = WebDriverWait(self.driver, 10)
        GoCheckout = waitElement.until(ec.presence_of_element_located(HHObjectClass.GoCheckout))
        return GoCheckout

    def mtGoPay(self):
        waitElement = WebDriverWait(self.driver, 10)
        GoPay = waitElement.until(ec.presence_of_element_located(HHObjectClass.GoPay))
        return GoPay

    def mtProfileBtn(self):
        waitElement = WebDriverWait(self.driver, 10)
        ProfileBtn = waitElement.until(ec.presence_of_element_located(HHObjectClass.ProfileBtn))
        return ProfileBtn

    def mtLogoutBtn(self):
        waitElement = WebDriverWait(self.driver, 10)
        LogoutBtn = waitElement.until(ec.presence_of_element_located(HHObjectClass.LogoutBtn))
        return LogoutBtn

    def generate_SS(self):
        timestamp = time.strftime("%Y%m%d%H%M%S")
        SS = self.driver.get_screenshot_as_file(timestamp + ".png")
        return SS
