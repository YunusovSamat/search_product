from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SearchProduct:
    __slots__ = ('driver',)

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://market.yandex.ru')
        # self.driver.get('https://market.yandex.ru/product--smartfon-xiaomi-redmi-6a-2-32gb/140070210/offers?track'
        #                 '=srchbtn&local-offers-first=0')

    def search(self, my_product):
        search_elem = self.driver.find_element_by_id('header-search')
        search_elem.send_keys(my_product)
        search_elem.send_keys(Keys.RETURN)
        links_product = self.driver.find_elements_by_css_selector('a.link_type_prices')
        # for l in links_product:
        #     print(l.text)
        links_product[0].click()


if __name__ == '__main__':
    sp = SearchProduct()
    sp.search('redmi 6a 32gb')
