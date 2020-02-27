from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time 
import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self,row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('user_list_table')
                rows = table.find_elements_by_tag_name('td')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)



    def test_user_can_get_website_then_calcualte_the_result_URL(self):
        #Henry want to use a calculator to solve a signal exercise
        #But he notice that his computer doesn't have any calculator program
        #His friend suggest the website for calcualte his exercise
        self.browser.get(self.live_server_url)

        #He notices the page title and header mention Calculator 
        self.assertIn('Calculator',self.browser.title)

        #He mention that there are description of website below title
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('Calculator',page_text)

        #He want to find result of 12345 + 12345 
        #Then he see two textboxs with "Enter your number".
        #So he enter 12345,12345 that he want to sum straight away.
        #He types "Signal" into a text box
        inputbox1 = self.browser.find_element_by_id('user_first_number')
        inputbox2 = self.browser.find_element_by_id('user_second_number')
        operation_dropdown = Select(self.browser.find_element_by_id('user_operator_type'))  
        button = self.browser.find_element_by_id('submit_button')
        self.assertEqual(
            inputbox1.get_attribute('placeholder'),
            'Enter your First Number'
        )
        self.assertEqual(
            inputbox2.get_attribute('placeholder'),
            'Enter your Second Number'
        )
        inputbox1.send_keys('12345')
        inputbox2.send_keys('12345')
        operation_dropdown.select_by_visible_text('Add(+)')  
        button.send_keys(Keys.ENTER)
        time.sleep(2)

        #After that he still see a ton of tutor user that agree 
        #to teach with that subject 
        table = self.browser.find_element_by_id('user_list_table')
        rows = table.find_elements_by_tag_name('td')
        self.assertIn('24690.0', [row.text for row in rows])
        time.sleep(1)


        self.fail('finist the test !!')
         

