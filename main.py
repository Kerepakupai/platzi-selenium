import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


class HelloWorld(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        options = webdriver.ChromeOptions()
        # options.add_argument('no-sandbox')
        # options.add_argument('--disable-gpu')
        options.add_argument('--headless')
        # options.add_argument('--disable-dev-shm-usage')
        service = ChromeService(executable_path='./chromedriver')
        cls.driver = webdriver.Chrome(service=service, options=options)
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self)->None:
        driver = self.driver
        driver.get('https://www.platzi.com')

    def test_open_farmaciasahumada(self)->None:
        self.driver.get('https://www.farmaciasahumada.cl')

    @classmethod
    def tearDown(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello-world-report'))
