import pytest, allure
from driver import startdriver
from pageElements import lenovo_product_page
from pageElements import lenovo_popup


@allure.story('Testing Reevoo modules on Lenovo product page')
class TestProductPage():
    start_page  = 'https://www.lenovo.com/gb/en/laptops/thinkpad/x-series/ThinkPad-X1-Carbon-6th-Gen/p/22TP2TXX16G'

    def setup(self):
        new_driver = startdriver.StartDriver()
        self.driver = new_driver.start()
        self.driver.implicitly_wait(15)
        self.driver.get(self.start_page)

    def teardown(self):
        self.driver.quit()

    @allure.feature('Find small elements on page Rating')
    def test_find_revoo_rating_small_bnt(self):
        with allure.step('Find Rating module on the page'):
            small_module = lenovo_product_page.ProductPage(self.driver).get_small_module_elements()
        with allure.step('Check module is visible for users'):
            assert small_module.is_displayed

    @allure.feature('Find Customer reviews rating on page')
    def test_reviews_score_not_a_null(self):
        with allure.step('Find Reviews Rating on the page'):
            reviews_score = lenovo_product_page.ProductPage(self.driver).get_product_rating()
        with allure.step('Check if Rating is visible and adequate values'):
            assert reviews_score is not None

    @allure.feature('Find Customer reviews total numbers')
    def test_check_total_reviews_numb(self):
        with allure.step('Find module on the page'):
            total_reviews = lenovo_product_page.ProductPage(self.driver).get_total_reviews_number()
        with allure.step('Find total reviews > 0 and on the page'):
            assert total_reviews > 0

    @allure.feature('Open Customer Reviews popup by clicking btn')
    def test_open_customer_review_popup(self):
        with allure.step('Find module on the page'):
            lenovo_popup.RevooPopup(self.driver).open_custom_reviews_popup()
        with allure.step('Click on the icon -> open the Pop Up'):
            popup = lenovo_popup.RevooPopup(self.driver).switch_to_customer_reviews_popup()
        with allure.step('Check if Pop Up is visible form users and its connected to Reevoo'):
            assert str(popup.get_attribute('title')) == 'Reevoo'

    @allure.feature('Check if Rating and Reviews number is in Customer Reviews popup')
    def test_rating_and_revirews_numb_in_popup(self):
        with allure.step('Get values from product page'):
            page_score = lenovo_product_page.ProductPage(self.driver).get_product_rating()
            page_reviews = lenovo_product_page.ProductPage(self.driver).get_total_reviews_number()
        with allure.step('Find module on the page'):
            lenovo_popup.RevooPopup(self.driver).open_custom_reviews_popup()
        with allure.step('Click on the icon -> open the Pop Up'):
            popup = lenovo_popup.RevooPopup(self.driver).switch_to_customer_reviews_popup()
        with allure.step('Check if Pop Up is visible form users and its connected to Reevoo'):
            assert str(popup.get_attribute('title')) == 'Reevoo'
        with allure.step('Check if Total review score in popup equeal to Product page'):
            popup_score = lenovo_popup.RevooPopup(self.driver).get_rating_from_popup()
            popup_reviews = lenovo_popup.RevooPopup(self.driver).get_total_reviews_num_from_popup()
            assert page_score == popup_score
            assert page_reviews == popup_reviews

    @allure.feature('Check scores')
    @pytest.mark.parametrize('score_params', ['Battery life',
                                              'Design',
                                              'Size and weight',
                                              'Performance',
                                              'Value for money',
                                              'Overall rating'])
    def test_custome_review_scores_eq_to_progress(self, score_params):


    def test_open_ask_owner_popup(self):
        pass
