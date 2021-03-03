# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login(self):
        driver = self.driver
        driver.get("http://testphp.vulnweb.com/login.php")
        driver.find_element_by_name("uname").click()
        driver.find_element_by_name("uname").clear()
        driver.find_element_by_name("uname").send_keys("test")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("test")
        driver.find_element_by_xpath("//input[@value='login']").click()
        driver.find_element_by_name("urname").click()
        driver.find_element_by_name("urname").clear()
        driver.find_element_by_name("urname").send_keys("Dexter")
        driver.find_element_by_name("ucc").clear()
        driver.find_element_by_name("ucc").send_keys("9876543211234")
        driver.find_element_by_name("uemail").clear()
        driver.find_element_by_name("uemail").send_keys("dexter@gmail.com")
        driver.find_element_by_name("uphone").clear()
        driver.find_element_by_name("uphone").send_keys("987654321")
        driver.find_element_by_name("uaddress").clear()
        driver.find_element_by_name("uaddress").send_keys("i am software tester")
        driver.find_element_by_name("update").click()
        driver.find_element_by_link_text("your cart").click()
        driver.find_element_by_link_text("Browse categories").click()
        driver.find_element_by_xpath("//div[@id='content']/div/a/h3").click()
        driver.find_element_by_xpath("//div[@id='content']/div/a/h3").click()
        driver.find_element_by_xpath("//input[@value='add this picture to cart']").click()
        driver.find_element_by_name("submitForm").click()
        driver.find_element_by_link_text("Back to homepage").click()
        driver.find_element_by_link_text("Logout test").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
