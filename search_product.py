import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SearchProduct:
    __slots__ = ('driver',)

    def __init__(self):
        self.driver = webdriver.Chrome()
        # self.driver.get('https://market.yandex.ru')
        self.driver.get('https://market.yandex.ru/product--smartfon-xiaomi-redmi-6a-2-32gb/140070210/offers?track'
                        '=srchbtn&local-offers-first=0')
        time.sleep(2)

    def search(self, my_product):
        search_elem = self.driver.find_element_by_id('header-search')
        search_elem.send_keys(my_product)
        search_elem.send_keys(Keys.RETURN)
        links_product = self.driver.find_elements_by_css_selector('a.link_type_prices')
        # for l in links_product:
        #     print(l.text)
        links_product[0].click()

    def choice(self):
        time.sleep(2)
        sorter_price = self.driver.find_element_by_xpath('/html/body/div[1]/div[6]/div[1]/div[2]/div[1]/div[1]/div[3]/a')
        sorter_price.click()
        time.sleep(3)
        cards = self.driver.find_elements_by_css_selector('div.n-snippet-card')
        products = list()
        for card in cards[:10]:
            card_price = card.find_element_by_css_selector('a.shop-history__link')
            link = card_price.get_attribute('href')
            price = card_price.text
            delivery = card.find_elements_by_css_selector('span.n-delivery__price')
            delivery = delivery[0][:-1] if delivery else 0
            print(delivery)

            # products.append((card_price.text, 0 if delivery else int(delivery[0]),
            #                  card_price.get_attribute('href')))


    # def write_to_file(self):
    #     with open('output.txt', 'w') as file:


    # def __del__(self):
    #     time.sleep(10)
    #     self.driver.close()


if __name__ == '__main__':
    sp = SearchProduct()
    sp.choice()
    # sp.search('redmi 6a 32gb')
    # sp.search('redmibook 14')

