"""
These tests cases cover Magazine Luiza searches for inexistent products.
"""

from pages.result import MagaluResultPage
from pages.search import MagaluSearchPage


def test_product_is_not_available(browser):
    search_page = MagaluSearchPage(browser)
    result_page = MagaluResultPage(browser)
    PHRASE = "nonexistentproduct"

    # Load Magazine Luiza page
    search_page.load()

    # Search for "Cerveja Corona"
    search_page.search(PHRASE)

    # Search value should be "Cerveja Corona"
    title = result_page.title()
    assert PHRASE == result_page.search_input_value()

    # Search results should be empty
    result_page.product_not_found_messages_visible()

    # Validate product not found messages
    message1 = result_page.product_not_found_message1()
    message2 = result_page.product_not_found_message2()
    assert 'Sua busca por' in message1
    assert ' não encontrou resultado algum :(' in message1
    assert 'Por favor, tente outra vez com termos menos específicos' in message2
