import re

class RevooPopup():
    def __init__(self, driver):
        self.driver = driver

    # We are using CSS locators
    page_locators = {
        'Prod_reviews': "div.reviews div.prodReview",
        'small_iframe': {
            'element': 'iframe[title*="Reviews"]',
            'review_module': 'div[data-reevoo-action="reviews"]',
            'review_rating_element': ' div[data-reevoo-action="reviews"] \
            div[class="reevoo__position--left"] reevoo-score', # get atribute data-score

            'reviews_number': 'div[class="reevoo__position--right"] div.reevoo__section--number-of-reviews', # Get text
            'ask_owner': 'div[data-reevoo-action="ask_an_owner"]'
        },
        'custome_revoews':{
            'iframe': 'iframe[title="CUSTOMER REVIEWS"]',
            'custome_review': 'a[id="reviews-tab-content-link"]',
            'total_reviews': 'div{class="product_details"] div.count-summary', # ? Get text
            'total_reviews_score': 'div[class="reevoo-score"] div.score-container reevoo-score', # Get attr data-score
            'scores': {
                'element': 'section[class="score_breakdown"] table tbody',
                'scores': 'section[class="score_breakdown"] table tbody tr'
            }
        },
        'ask_owner': {
            'iframe': 'iframe[title="ASK AN OWNER"]',
        }
    }

    def get_product_rating(self):
        self.driver.switch_to.frame(self.page_locators['small_iframe'])
        r = self.driver.find_elemnt_by_css_selector(self.page_locators['small_iframe']['review_rating_element'])
        return r.get_attribute('data-score')

    def get_total_reviews_number(self):
        self.driver.switch_to.frame(self.page_locators['small_iframe'])
        total_reviews = self.driver.find_element_by_css_selector(self.page_locators['small_iframe']['reviews_number'])

        # re fro regular expression , get only numbers
        return re.findall('\d+', total_reviews)

    def open_reviews_popup(self):
        self.driver.switch_to.frame(self.page_locators['small_iframe'])
        self.driver.find_element_by_css_selector(self.page_locators['small_iframe']['review_module']).click()
        self.driver.switch_to.frame(self.page_locators['custome_revoews']['iframe'])

    def open_ask_owner_popup(self):
        self.driver.switch_to.frame(self.page_locators['small_iframe'])
        self.driver.find_element_by_css_selector(self.page_locators['small_iframe']['ask_owner']).click()
        self.driver.switch_to.frame(self.page_locators['ask_owner']['iframe'])

