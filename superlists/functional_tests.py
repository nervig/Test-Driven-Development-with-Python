from selenium import webdriver
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
        self.fail('Finish test!')


# To her immediately is suggested to enter a unit of list
# She types in a text field "Buy a new flash drive"

# When she push on enter, the page is reloading, and now the page contains
# "1: Buy a new flash drive" as a unit of item of list

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
