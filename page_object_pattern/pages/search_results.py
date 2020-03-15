class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver
        self.ofert_names = "//h3[contains(@class,'margin-clear bold')]//a"
        self.ofert_prices = "//div[contains(@class,'mt-20')]//span"

    def get_offer_names(self):
        oferts = self.driver.find_elements_by_xpath(self.ofert_names)
        return [ofert.get_attribute("textContent") for ofert in oferts]

    def get_ofert_prices(self):
        prices = self.driver.find_elements_by_xpath(self.ofert_prices)
        return [price.get_attribute("textContent") for price in prices]
