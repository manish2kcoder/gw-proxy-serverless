import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.common.by import By
import time


class TestClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe")
        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(20)
        self.driver.maximize_window()

    def test_FormSubmission_Pass(self):
        self.driver.get("https://glasswallsolutions.com/evaluation/")
        headerTitle = self.driver.title
        print(headerTitle)
        iframe = self.driver.find_element_by_id("hs-form-iframe-0")
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_xpath("//*[@id='firstname-c554841d-4168-40f5-8068-a1046f0eaed0']").send_keys(
            "Tester")
        self.driver.find_element_by_xpath("//*[@id='email-c554841d-4168-40f5-8068-a1046f0eaed0']").send_keys(
            "Tester@tester.com")
        self.driver.find_element_by_xpath(
            "//*[@id='LEGAL_CONSENT.subscription_type_4771533-c554841d-4168-40f5-8068-a1046f0eaed0']").click()
        self.driver.find_element_by_xpath(
            "//*[@id='hsForm_c554841d-4168-40f5-8068-a1046f0eaed0']/div[6]/div[2]/input").submit()
        successMessage = self.driver.find_element_by_xpath("/html/body/div/div/p[3]/a")
        print(successMessage.text)
        self.assertEqual(successMessage.text, "BACK TO SITE", "Form not submitted")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()









