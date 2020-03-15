from selenium.webdriver.support.select import Select

class SearchKitePage:
    def __init__(self, driver):
        self.driver = driver
        self.details = "show_advanced_searchform"
        self.category = "id_category"
        self.model_kite = "keyword"
        self.company_choice = "id_factory"
        self.min_price_range = "id_price_0"
        self.max_price_range = "id_price_1"
        self.min_year_range = "id_year_0"
        self.max_year_range = "id_year_1"
        self.min_kite_size_range = "id_kitesize_0"
        self.max_kite_size_range = "id_kitesize_1"
        self.button_click = "//button[@type='submit']"

    def set_detail(self):
        self.driver.find_element_by_id(self.details).click()

    def set_category2(self, value):
        # self.id_cat = self.driver.find_element_by_id(self.category).click()
        self.id_cat = Select(self.driver.find_element_by_id(self.category))
        self.id_cat.select_by_value(value)

    def set_model_kite(self,model_name):
        self.driver.find_element_by_name(self.model_kite).click()
        self.driver.find_element_by_name(self.model_kite).clear()
        self.driver.find_element_by_name(self.model_kite).send_keys(model_name)

    def set_company_name(self, company_name):
        self.driver.find_element_by_id(self.company_choice).click()
        self.company_select = Select(self.driver.find_element_by_id(self.company_choice))
        self.company_select.select_by_visible_text(company_name)

    def set_price_range(self, min_price, max_price):
        self.driver.find_element_by_id(self.min_price_range).send_keys(min_price)
        self.driver.find_element_by_id(self.max_price_range).send_keys(max_price)

    def set_year_prod_range(self, from_year, to_year):
        self.year_from_select = Select(self.driver.find_element_by_id(self.min_year_range))
        self.year_from_select.select_by_value(from_year)
        self.year_to_select = Select(self.driver.find_element_by_id(self.max_year_range))
        self.year_to_select.select_by_value(to_year)

    def set_size_range(self, from_size, to_size):
        self.select_min = Select(self.driver.find_element_by_id(self.min_kite_size_range))
        self.select_min.select_by_value(from_size)
        self.select_max = Select(self.driver.find_element_by_id(self.max_kite_size_range))
        self.select_max.select_by_value(to_size)

    def click_button(self):
        self.driver.find_element_by_xpath(self.button_click).click()






