"""
This module contains MagaluResultPage,
the page object for the Magalu search result page.
"""

import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MagaluResultPage:

    # Locators
    RESULT_LINKS = (By.XPATH, '//li[@class="nm-product-item"]/a')
    SEARCH_INPUT = (By.ID, 'inpHeaderSearch')
    RESULT_HEADER = (By.XPATH, '//h1[@id="main-title"]')
    NO_RESULTS_FOUND_MESSAGE_1 = (By.CSS_SELECTOR, 'div.nm-not-found-message1')
    NO_RESULTS_FOUND_MESSAGE_2 = (By.CSS_SELECTOR, 'div.nm-not-found-message2')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    def result_links(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        return links

    def result_link_titles(self, links):
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.browser.title

    def choose_random_item(self, links):
        item = random.choice(links)
        return item

    def result_link_title(self, link):
        return link.text

    def click_result_item(self, item):
        item.click()

    def click_random_item(self, links):
        item = self.choose_random_item(links)
        chosen_item_title = self.result_link_title(item)
        self.click_result_item(item)
        return chosen_item_title

    def wait_results_to_load(self):
        result_input = self.browser.find_element(*self.RESULT_HEADER)
        WebDriverWait(self.browser, 10).until(expected_conditions.visibility_of(result_input))

    def product_not_found_messages_visible(self):
        message1 = self.browser.find_element(*self.NO_RESULTS_FOUND_MESSAGE_1)
        message2 = self.browser.find_element(*self.NO_RESULTS_FOUND_MESSAGE_2)
        WebDriverWait(self.browser, 10).until(expected_conditions.visibility_of(message1))
        WebDriverWait(self.browser, 10).until(expected_conditions.visibility_of(message2))

    def product_not_found_message1(self):
        message1 = self.browser.find_element(*self.NO_RESULTS_FOUND_MESSAGE_1)
        message1.text()
        return value

    def product_not_found_message1(self):
        message2 = self.browser.find_element(*self.NO_RESULTS_FOUND_MESSAGE_2)
        value = message2.text()
        return value
