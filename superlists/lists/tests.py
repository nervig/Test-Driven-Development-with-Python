from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

class HomePageTest(TestCase):
    '''test of home page'''

    def test_root_url_resolves_to_home_page_view(self):
        '''test: root url converted to image of home page'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)

