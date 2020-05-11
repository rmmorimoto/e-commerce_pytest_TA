"""
This module contains MagaluProductPage,
the page object for the Magalu product page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class MagaluProductPage:

    # Locators
    ADD_TO_CART_BUTTON = '//button[contains(@class, "button__buy")]'

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def title(self):
        return self.browser.title

    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element_by_xpath(self.ADD_TO_CART_BUTTON)
        #WebDriverWait(self.browser, 5).until(expected_conditions.element_to_be_clickable(*self.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()
