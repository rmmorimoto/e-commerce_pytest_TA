"""
This module contains MagaluSearchPage,
the page object for the Magalu search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MagaluSearchPage:

  # URL
  URL = 'https://www.magazineluiza.com.br'

  # Locators
  SEARCH_INPUT = (By.ID, 'inpHeaderSearch')

  # Initializer
  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods
  def load(self):
    self.browser.get(self.URL)

  def search(self, phrase):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    search_input.send_keys(phrase + Keys.RETURN)
