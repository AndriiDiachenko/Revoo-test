import re


class ProductPage():

    def __init__(self, driver):
        self.driver = driver

    page_locators = {
        'prod_reviews': "div.reviews div.prodReview",
        'small_iframe': {
            'element': 'iframe[title*="Reviews"]',
            'review_module': 'div[data-reevoo-action="reviews"]',
            'review_rating_element': ' div[data-reevoo-action="reviews"] \
        div[class="reevoo__position--left"] reevoo-score',  # get atribute data-score

            'reviews_number': 'div[class="reevoo__position--right"] div.reevoo__section--number-of-reviews',  # Get text
            'ask_owner': 'div[data-reevoo-action="ask_an_owner"]'
        }
    }

    def get_small_module_elements(self):
        return self.driver.find_element_by_css_selector(self.page_locators['prod_reviews'])

    def get_product_rating(self):
        self.driver.switch_to.frame(self.page_locators['small_iframe'])
        r = self.driver.find_elemnt_by_css_selector(self.page_locators['small_iframe']['review_rating_element'])
        return r.get_attribute('data-score')

    def get_total_reviews_number(self):
        self.driver.switch_to.frame(self.page_locators['small_iframe'])
        total_reviews = self.driver.find_element_by_css_selector(self.page_locators['small_iframe']['reviews_number'])

        # re fro regular expression , get only numbers
        return re.findall('\d+', total_reviews.text)
