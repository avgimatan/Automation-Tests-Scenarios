'''
Scenario2: apply a resume
    1) press on the Job button
    2) type on the search tab the desirable job
    3) the system present the results
    4) the user choose which job interesting him
    5) the user press on the apply button
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ApplyResume(unittest.TestCase):

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

    def test_job_search(self):

        driver = self.driver

        # Job button
        enter_job_site = driver.find_element_by_xpath('//*[@id="jobs-tab-icon"]')
        enter_job_site.click()

        driver.get("https://www.linkedin.com/jobs/")

        # Search input label
        search_input_label = driver.find_element_by_xpath('//*[@id="jobs-search-box-keyword-id-ember37"]')
        search_input_label.send_keys("QA Automation student")
        driver.implicitly_wait(5)
        search_input_label.send_keys(Keys.RETURN)

        driver.implicitly_wait(10)

        jobs = driver.find_elements_by_class_name('occludable-update artdeco-list__item--offset-4 artdeco-list__item p0 ember-view')
        print(jobs)
        print(type(jobs))
        self.assertGreater(len(jobs),
                           0)

    def test_apply_resume(self):

        driver = self.driver
        job_url = driver.get('https://www.linkedin.com/jobs/search/?geoId=101620260&keywords=qa%20automation%20student&location=Israel')
        driver.implicitly_wait(5)
        apply_button = driver.find_element_by_xpath('//*[@id="ember315"]')

        apply_button.submit()

        self.assertIsNot(job_url,
                         driver.current_url,
                         msg='stays in the same page')

    @classmethod
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
