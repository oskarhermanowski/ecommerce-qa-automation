from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.chechkout_page import CheckoutPage

def test_complete_checkout(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    # Login
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Add product
    inventory_page.add_backpack_to_cart()

    # Open cart
    inventory_page.open_cart()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(cart_page.product_name).to_have_text("Sauce Labs Backpack")

    # Checkout
    cart_page.checkout()

    checkout_page.fill_customer_data(
    "Oskar",
    "Tester",
    "00-001"
)

    checkout_page.continue_checkout()
    checkout_page.finish_order()

    expect(checkout_page.complete_header).to_have_text(
    "Thank you for your order!"
)