'''

Scenario3: update user profile
    1) enter to user profile
    2) press on edit button
    3) the user choose what to edit
    4) write the new text
    5) press save button

'''


import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class UpdateUserProfile(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\Users\mmavg\chromedriver\chromedriver.exe")
        driver = self.driver
        driver.get("https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin")

        username = driver.find_element_by_id("username")
        password = driver.find_element_by_id("password")
        submit = driver.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')

        username.send_keys("the_username")
        password.send_keys("the_password")

        submit.click()

        driver.implicitly_wait(5)

    def test_update_user_name(self):
        driver = self.driver

        dropdown = driver.find_element_by_xpath('//*[@id="nav-settings__dropdown-trigger"]/div/li-icon')
        dropdown.click()
        driver.implicitly_wait(5)

        see_profile = driver.find_element_by_xpath('//*[@id="ember4201"]/div[2]/span')
        see_profile.click()

        edit_button = driver.find_element_by_xpath('//*[@id="ember4237"]')
        edit_button.click()

        new_first_name = 'Tav'
        new_last_name = 'Beza'
        first_name_input = driver.find_element_by_id('topcard-firstname')
        first_name_input.send_keys(new_first_name)
        last_name_input = driver.find_element_by_id('topcard-lastname')
        last_name_input.send_keys(new_last_name)

        save_change = driver.find_element_by_class_name('pe-form-footer__action--submit artdeco-button form-submit-action t-14 t-white t-normal')
        save_change.click()

        get_new_input_name = driver.find_element_by_xpath('//*[@id="topcard-firstname"]').text()

        self.assertEqual(get_new_input_name,
                         new_first_name + ' ' + new_last_name,
                         msg='Edit profile failed')

    @classmethod
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
