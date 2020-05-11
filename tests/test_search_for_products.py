"""
These tests cases cover Magazine Luiza searches for specific products.
"""

from pages.product import MagaluProductPage
from pages.result import MagaluResultPage
from pages.search import MagaluSearchPage
from pages.shopping_cart import MagaluShoppingCartPage


def test_select_product_and_validate_in_cart(browser):
    search_page = MagaluSearchPage(browser)
    result_page = MagaluResultPage(browser)
    product_page = MagaluProductPage(browser)
    shopping_cart_page = MagaluShoppingCartPage(browser)
    PHRASE = "Cerveja Corona"

    # Load Magazine Luiza page
    search_page.load()

    # Search for "Cerveja Corona"
    search_page.search(PHRASE)

    # Search value should be "Cerveja Corona"
    title = result_page.title()
    assert PHRASE == result_page.search_input_value()

    # Search results should contain "Cerveja Corona""
    result_page.wait_results_to_load()
    links = result_page.result_links()
    titles = result_page.result_link_titles(links)
    matches = [t for t in titles if PHRASE.lower() in t.lower()]
    assert len(matches) > 0

    # Select a random result and click on it
    item_title = result_page.click_random_item(links)

    # Add product to the shopping cart
    title = product_page.title()
    product_page.add_to_cart()

    # Validate that shopping cart page is open
    shopping_cart_page.wait_shopping_cart_page()
    assert 'Sacola de compras' in shopping_cart_page.title()

    # Validate product in shopping cart
    links = shopping_cart_page.shopping_cart_item_links()
    titles = shopping_cart_page.shopping_cart_item_link_titles(links)
    matches = [t for t in titles if PHRASE.lower() in t.lower()]
