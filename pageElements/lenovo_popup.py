from lenovo_product_page import ProductPage as pp

class RevooPopup():
    def __init__(self, driver):
        self.driver = driver

    # We are using CSS locators
    page_locators = {
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



    def open_custom_reviews_popup(self):
        self.driver.switch_to.frame(pp.page_locators['small_iframe'])
        self.driver.find_element_by_css_selector(self.page_locators['small_iframe']['review_module']).click()
        self.driver.switch_to.frame(self.page_locators['custome_revoews']['iframe'])

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



