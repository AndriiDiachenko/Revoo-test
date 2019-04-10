import re


class ProductPage():

    def __init__(self, driver):
        self.driver = driver

    page_locators = {
        'prod_reviews': "div.reviews div.prodReview",
        'small_iframe': {
            'element': 'iframe[title*="Reviews"]',
            'review_module': 'div[data-reevoo-action="reviews"]',
            'review_rating_element': 'div[data-reevoo-action="reviews"] \
        div[class="reevoo__position--left"] reevoo-score',  # get atribute data-score
            'reviews_number': 'div[data-reevoo-action="reviews"] \
             div[class="reevoo__position--right"] div[class="reevoo__section--number-of-reviews"]',  # Get text
            'ask_owner': 'div[data-reevoo-action="ask_an_owner"]'
        }
    }

    def get_small_module_elements(self):
        return self.driver.find_element_by_css_selector(self.page_locators['prod_reviews'])

    def get_product_rating(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector(self.page_locators['small_iframe']['element']))
        r = self.driver.find_element_by_css_selector(self.page_locators['small_iframe']['review_rating_element'])
        return r.get_attribute('data-score')

    def get_total_reviews_number(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector(self.page_locators['small_iframe']['element']))
        total_reviews = self.driver.find_element_by_css_selector(self.page_locators['small_iframe']['reviews_number'])
        print(total_reviews)
        # re fro regular expression , get only numbers
        reviews_count = re.findall(r'\d+', total_reviews.text)[0]
        return int(reviews_count)
