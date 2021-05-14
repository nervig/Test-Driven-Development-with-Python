from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    '''a test of new visitor'''

    def setUp(self):
        '''setup'''
        self.browser = webdriver.Firefox()

    def tearDown(self):
        '''retrieve'''
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''test: can start a list and get his it later'''
        # Elin heard about cool new online-app with
        # list of urgent tasks. She decided to estimate his home page.
        self.browser.get('http:/localhost:8000')

        # She sees, what a title and header tell about lists urgent tasks.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # To her immediately is suggested to enter a unit of list
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types in a text field "Buy a new flash drive"
        inputbox.send_keys('Buy flash drive')

        # When she push on enter, the page is reloading, and now the page contains
        # "1: Buy a new flash drive" as a unit of item of list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy flash drive' for row in rows)
        )
        self.fail('Finish the test!')
# The field of text still invites her to add yet one element.
# She enters "To make a write on flash drive"

# The page again reload and now shows both elements of her list.

# Elin be interesting, the site will remember the list of her? Then she sees,
# that the site has generated the unical url-address for her -
# about this it is showing a little text with explains.

# She visits this URL-address - it is list of she still there.

# Satisfied with the result, she go to the bed.
if __name__ == '__main__':
    unittest.main(warnings='ignore')
