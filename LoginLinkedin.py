'''

Scenario1: Login to linkedin
    1) the user enters to Linkedin
    3) the user enters the password and user id
    4) the system checks the user details
    5) the user log into the site

'''

import unittest

# Import the Selenium 2 module (aka "webdriver")
from selenium import webdriver


class LoginTestCase(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\Users\mmavg\chromedriver\chromedriver.exe")

    def test_login_linkedin(self):
        driver = self.driver
        driver.get("https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin")
        home_page = "https://www.linkedin.com/feed/?trk=guest_homepage-basic_nav-header-signin"

        username = driver.find_element_by_id("username")
        password = driver.find_element_by_id("password")
        submit = driver.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')

        username.send_keys("the_username")
        password.send_keys("the_password")

        submit.click()

        driver.implicitly_wait(5)

        self.assertEqual(
            driver.current_url,
            home_page,
            msg="Successful Login"
        )

    @classmethod
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
