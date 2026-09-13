from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_product_to_cart(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(inventory_page.page_title).to_have_text("Products")

    inventory_page.add_backpack_to_cart()

    expect(inventory_page.cart_badge).to_have_text("1")

def test_sort_products_price_low_to_high(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(inventory_page.page_title).to_have_text("Products")

    inventory_page.sort_products("lohi")

    prices = inventory_page.get_product_prices()

    assert prices == sorted(prices)

def test_sort_products_price_high_to_low(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.sort_products("hilo")

    prices = inventory_page.get_product_prices()

    assert prices == sorted(prices, reverse=True)


def test_sort_products_name_a_to_z(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.sort_products("az")

    names = inventory_page.get_product_names()

    assert names == sorted(names)


def test_sort_products_name_z_to_a(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.sort_products("za")

    names = inventory_page.get_product_names()

    assert names == sorted(names, reverse=True)
