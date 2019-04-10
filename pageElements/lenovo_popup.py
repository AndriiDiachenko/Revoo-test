from pageElements.lenovo_product_page import ProductPage as pp
import re

class RevooPopup():
    def __init__(self, driver):
        self.driver = driver

    # We are using CSS locators
    page_locators = {
        'small_iframe': {
            'element': 'iframe[title*="Reviews"]',
            'review_module': 'div[data-reevoo-action="reviews"]'
        },
        'custom_reviews':{
            'element': 'iframe[title="CUSTOMER REVIEWS"]',
            'custom_review': 'a[id="reviews-tab-content-link"]',
            'total_reviews': 'div[class="count-summary"]', # ? Get text
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



    def open_custom_reviews_popup(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector(self.page_locators['small_iframe']['element']))
        self.driver.find_element_by_css_selector(self.page_locators['small_iframe']['review_module']).click()

    def switch_to_customer_reviews_popup(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector(self.page_locators['custom_reviews']['element']))
        return self.driver.find_element_by_css_selector('nav[class="tabs"] header img')

    def get_rating_from_popup(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector(self.page_locators['custom_reviews']['element']))
        rating =  self.driver.find_element_by_css_selector(self.page_locators['custom_reviews']['total_reviews_score'])
        return rating.get_attribute('data-score')

    def get_total_reviews_num_from_popup(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_element_by_css_selector(self.page_locators['custom_reviews']['element']))
        total_reviews = self.driver.find_element_by_css_selector(self.page_locators['custom_reviews']['total_reviews'])
        reviews_count = re.findall(r'\d+', total_reviews.text)[0]
        return int(reviews_count)

    def open_ask_owner_popup(self):
        self.driver.switch_to.frame(pp.page_locators['small_iframe'])
        self.driver.find_element_by_css_selector(self.page_locators['small_iframe']['ask_owner']).click()
        self.driver.switch_to.frame(self.page_locators['ask_owner']['iframe'])

    def custom_reviews_scores_table(self):
        self.driver.switch_to.frame(self.page_locators['custome_revoews']['iframe'])
        scores = self.driver.find_elements_by_css_selector(self.page_locators['custome_revoews']['scores'])
        score_dict = {}
        for score in scores:
            score_title = score.find_element_by_css_selector('th[scope="row"]').text
            score_vale = score.find_element_by_css_selector('td[data-score]').get_attribute('data-score')
            score_dict[score_title] = score_vale



