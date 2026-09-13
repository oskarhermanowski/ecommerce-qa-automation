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