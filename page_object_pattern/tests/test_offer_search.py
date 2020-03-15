import pytest
from selenium import webdriver
from page_object_pattern.pages.search_kite import SearchKitePage
from page_object_pattern.pages.search_results import SearchResultsPage

class TestOfferSearch:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(r'C:\Users\gonta\PycharmProjects\Selenium\seleniumddemo\chromedriver.exe')
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_offer_search(self,setup):
        self.driver.get('https://www.getakite.de')
        search_offer_search = SearchKitePage(self.driver)
        search_offer_search.set_detail()
        search_offer_search.set_category2('1')
        # search_offer_search.model_kite("Soul")
        search_offer_search.set_company_name('Flysurfer')
        search_offer_search.set_price_range('1000','1800')
        search_offer_search.set_year_prod_range('18','21')
        search_offer_search.set_size_range('34','37')
        search_offer_search.click_button()
        results_page = SearchResultsPage(self.driver)
        offer_names = results_page.get_offer_names()
        offer_prices = results_page.get_ofert_prices()

        print(offer_names)
        print(offer_prices)


