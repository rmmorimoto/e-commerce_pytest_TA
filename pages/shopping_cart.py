"""
This module contains MagaluShoppingCartPage,
the page object for the Magalu shopping cart page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MagaluShoppingCartPage:

    # Locators
    PRODUCT_TITLES = (By.CSS_SELECTOR, 'a.BasketItemProduct-info-title')
    SHOPPING_CART_PAGE_TITLE = (By.XPATH, '//div[@class="BasketPage-title"]')
    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def shopping_cart_item_links(self):
        links = self.browser.find_elements(*self.PRODUCT_TITLES)
        return links

    def shopping_cart_item_link_titles(self, links):
        titles = [link.text for link in links]
        return titles

    def title(self):
        return self.browser.title

    def wait_shopping_cart_page(self):
        page_title = self.browser.find_element(*self.SHOPPING_CART_PAGE_TITLE)
        WebDriverWait(self.browser, 10).until(expected_conditions.visibility_of(page_title))
