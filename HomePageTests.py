'''
Scanerio4: test home page functionality
'''


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePageTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(r"C:\Users\mmavg\chromedriver\chromedriver.exe")
        driver = cls.driver
        driver.get("https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin")

        username = driver.find_element_by_id("username")
        password = driver.find_element_by_id("password")
        submit = driver.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')

        username.send_keys("the_username")
        password.send_keys("the_password")

        submit.click()

        driver.implicitly_wait(5)

    def test_search_box(self):

        self.assertTrue(self.is_element_present(By.XPATH, '//*[@id="ember33"]/input'))

    def test_post_window(self):
        driver = self.driver
        write_post_button = driver.find_element_by_class_name('share-box__open share-box__trigger p4 hoverable-link-text t-16 t-black--light t-bold')
        write_post_button.click()

        self.assertTrue(self.is_element_present(By.CLASS_NAME, 'mentions-texteditor__content'))

    def test_no_notification(self):

        notification_button = self.driver.find_element_by_xpath('//*[@id="notifications-tab-icon"]')
        notification_button.click()

        notification_msg = self.driver.find_element_by_xpath('//*[@id="ember50"]/div/div[1]/p').text()

        self.assertEqual(notification_msg,
                         "You’re all caught up! Check back later for new notifications",
                         msg="check your notification")

    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()