import time
import random

from utilities.BaseClass import BaseClass
from DynamicObjects.NormalItemObjects import NormalItemObjectClass
from DynamicObjects.DealItemObjects import DealObjectClass
from DynamicObjects.NormalItemWithItemOptionObjects import NormalItemOption
from DynamicObjects.HHItemObjects import HHObjectClass


class TestDynamicItem(BaseClass):

    def test_mtDynamicItems(self):
        item = ["normal", "deal", "item_option", "HH"]

        def mtNormalItem():
            OO_Object = NormalItemObjectClass(self.driver)
            OO_Object.mtLogin().click()
            OO_Object.mtemail().send_keys("vin.cuenza@easypos.com.ph")
            OO_Object.mtpassword().send_keys("Aa1234567890")
            # OO_Object.generate_SS()
            OO_Object.mtLoginBtn().click()
            time.sleep(5)
            OO_Object.mtScrollDown()
            time.sleep(1)
            OO_Object.mtItemSelected01().click()
            time.sleep(2)
            OO_Object.mtAddItem01().click()
            OO_Object.mtViewCart().click()
            time.sleep(1)
            # OO_Object.generate_SS()
            OO_Object.mtGoCheckout().click()
            time.sleep(10)
            # OO_Object.generate_SS()
            OO_Object.mtGoPay().click()
            OO_Object.generate_SS()
            time.sleep(5)
            OO_Object.mtProfileBtn().click()
            time.sleep(1)
            OO_Object.mtLogoutBtn().click()
            time.sleep(3)
            return print("this is normal item")

        def mtDealItem():
            Deal_Object = DealObjectClass(self.driver)

            Deal_Object.mtLogin().click()
            Deal_Object.mtemail().send_keys("vin.cuenza@easypos.com.ph")
            Deal_Object.mtpassword().send_keys("Aa1234567890")
            Deal_Object.generate_SS()
            Deal_Object.mtLoginBtn().click()
            time.sleep(5)
            Deal_Object.mtScrollDown()

            # Select Deal from Menu
            time.sleep(1)
            Deal_Object.mtDealMenuSelect01().click()
            time.sleep(2)
            Deal_Object.generate_SS()

            # DEAL SELECTION PROCESS
            # 1
            Deal_Object.mtDealSelection01().click()
            time.sleep(1)
            Deal_Object.mtDealSelected01().click()
            time.sleep(1)
            Deal_Object.mtDealSelectedBtn01().click()
            time.sleep(1)
            Deal_Object.generate_SS()
            # 1

            # 2
            Deal_Object.mtDealSelection02().click()
            time.sleep(1)
            Deal_Object.mtDealSelected02().click()
            time.sleep(2)
            # Deal_Object.mtDealSelectedBtn02().click()
            time.sleep(1)
            Deal_Object.generate_SS()
            # 2
            # DEAL SELECTION PROCESS

            # ADD DEAL
            Deal_Object.mtDealMenuSelectBtn01().click()

            # PROCESS TO PAY ORDER
            Deal_Object.mtViewCart().click()
            time.sleep(1)
            Deal_Object.generate_SS()
            Deal_Object.mtGoCheckout().click()
            time.sleep(10)
            Deal_Object.generate_SS()
            Deal_Object.mtGoPay().click()
            Deal_Object.generate_SS()
            # PROCESS TO PAY ORDER
            time.sleep(5)
            Deal_Object.mtProfileBtn().click()
            time.sleep(1)
            Deal_Object.mtLogoutBtn().click()
            time.sleep(3)
            return print("this is deal item")

        def mtItemOption():
            NIO_Object = NormalItemOption(self.driver)
            NIO_Object.mtLogin().click()
            NIO_Object.mtemail().send_keys("vin.cuenza@easypos.com.ph")
            NIO_Object.mtpassword().send_keys("Aa1234567890")
            # OO_Object.generate_SS()
            NIO_Object.mtLoginBtn().click()
            time.sleep(5)
            NIO_Object.mtScrollDown()
            time.sleep(1)
            NIO_Object.mtItemSelected01().click()
            time.sleep(2)
            NIO_Object.mtItemOption01().click()
            NIO_Object.mtAddItem01().click()
            NIO_Object.mtViewCart().click()
            time.sleep(1)
            # OO_Object.generate_SS()
            NIO_Object.mtGoCheckout().click()
            time.sleep(10)
            # OO_Object.generate_SS()
            NIO_Object.mtGoPay().click()
            NIO_Object.generate_SS()
            time.sleep(5)
            NIO_Object.mtProfileBtn().click()
            time.sleep(1)
            NIO_Object.mtLogoutBtn().click()
            time.sleep(3)
            return print("this is item option")

        def mtHH():
            HH_Object = HHObjectClass(self.driver)
            HH_Object.mtLogin().click()
            HH_Object.mtemail().send_keys("vin.cuenza@easypos.com.ph")
            HH_Object.mtpassword().send_keys("Aa1234567890")
            # OO_Object.generate_SS()
            HH_Object.mtLoginBtn().click()
            time.sleep(5)
            HH_Object.mtScrollDown()
            time.sleep(1)

            # HH Item Select
            HH_Object.mtHHSelect01().click()
            time.sleep(2)

            # 1st half
            HH_Object.mtClick1stHalf().click()
            time.sleep(1)
            HH_Object.mtClick1stHalfPizza().click()
            time.sleep(1)
            HH_Object.mtFinished1stPizza().click()
            time.sleep(1)

            # 2nd Click
            HH_Object.mtClick2ndHalf().click()
            time.sleep(1)
            HH_Object.mtClick2ndHalfPizza().click()
            time.sleep(1)
            HH_Object.mtFinished2ndPizza().click()
            time.sleep(1)
            HH_Object.mtAddItem01().click()
            time.sleep(1)

            # Process Order
            HH_Object.mtViewCart().click()
            time.sleep(1)
            # OO_Object.generate_SS()
            HH_Object.mtGoCheckout().click()
            time.sleep(10)
            # OO_Object.generate_SS()
            HH_Object.mtGoPay().click()
            HH_Object.generate_SS()
            time.sleep(5)

            # Logout
            HH_Object.mtProfileBtn().click()
            time.sleep(1)
            HH_Object.mtLogoutBtn().click()
            time.sleep(3)
            return print("this is HH item")

        enumsample = {
            "normal": mtNormalItem,
            "deal": mtDealItem,
            "item_option": mtItemOption,
            "HH": mtHH
        }

        for i in range(50):
            random_item = random.choice(item)
            enumsample[random_item]()
