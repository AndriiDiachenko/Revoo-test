import pytest
from driver import startdriver
from pageElements import lenovo_product_page
import time

class TestProductPage():
    start_page  = 'https://www.lenovo.com/gb/en/laptops/thinkpad/x-series/ThinkPad-X1-Carbon-6th-Gen/p/22TP2TXX16G'

    def setup(self):
        new_driver = startdriver.StartDriver()
        self.driver = new_driver.start()
        self.driver.implicitly_wait(15)
        self.driver.get(self.start_page)

    def teardown(self):
        self.driver.quit()

    def test_find_revoo_rating_small_bnt(self):
        small_module = lenovo_product_page.ProductPage(self.driver).get_small_module_elements()
        assert small_module.is_displayed

    def test_reviews_score_not_a_null(self):
        reviews_score = lenovo_product_page.ProductPage(self.driver).get_product_rating()
        assert reviews_score