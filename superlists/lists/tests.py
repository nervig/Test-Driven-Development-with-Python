from django.test import TestCase

class SmokeTest(TestCase):
    '''test of toxic'''

    def test_bad_maths(self):
        '''incorrect math calculation'''
        self.assertEqual(1 + 1, 3)

