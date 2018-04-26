import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    """
    A test class for functional testing of THcrm
    """

    def setUp(self):
        self.browser = webdriver.Chrome()
    #
    # def tearDown(self):
    #     self.browser.quit()

    def test_can_view_home_page(self):
        self.browser.get("http://localhost:8000/")
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main(warnings='ignore')