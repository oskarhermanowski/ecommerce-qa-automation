from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_product_is_visible_in_cart(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    # Login
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Add product
    inventory_page.add_backpack_to_cart()

    # Open Cart
    inventory_page.open_cart()

    # Verify product
    expect(cart_page.cart_item).to_have_count(1)
    expect(cart_page.product_name).to_have_text("Sauce Labs Backpack")

def test_remove_product_from_cart(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    expect(cart_page.cart_item).to_have_count(1)

    cart_page.remove_backpack()

    expect(cart_page.cart_item).to_have_count(0)

def test_continue_shopping_from_cart(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page.continue_shopping()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(inventory_page.page_title).to_have_text("Products")

def test_add_multiple_products_to_cart(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()

    expect(inventory_page.cart_badge).to_have_text("2")

    inventory_page.open_cart()

    expect(cart_page.cart_item).to_have_count(2)