import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_complete_checkout(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    # Add product
    inventory_page.add_backpack_to_cart()

    # Open cart
    inventory_page.open_cart()
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/cart.html")
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

@pytest.mark.parametrize(
    "first_name,last_name,postal_code,expected_message",
    [
        ("", "Tester", "00-001", "Error: First Name is required"),
        ("Oskar", "", "00-001", "Error: Last Name is required"),
        ("Oskar", "Tester", "", "Error: Postal Code is required"),
    ],
)

def test_checkout_validation_error(
    logged_in_page: Page,
    first_name,
    last_name,
    postal_code,
    expected_message,
):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page.checkout()

    checkout_page.fill_customer_data(
        first_name,
        last_name,
        postal_code
    )

    checkout_page.continue_checkout()

    expect(checkout_page.error_message).to_have_text(expected_message)

def test_checkout_price_summary(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page.checkout()

    checkout_page.fill_customer_data(
        "Oskar",
        "Tester",
        "00-001"
    )

    checkout_page.continue_checkout()

    expect(checkout_page.item_price).to_have_text("$29.99")
    expect(checkout_page.subtotal).to_have_text("Item total: $29.99")
    expect(checkout_page.tax).to_have_text("Tax: $2.40")
    expect(checkout_page.total).to_have_text("Total: $32.39")

def test_checkout_total_calculation(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = CheckoutPage(logged_in_page)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page.checkout()

    checkout_page.fill_customer_data(
        "Oskar",
        "Tester",
        "00-001"
    )

    checkout_page.continue_checkout()

    item_price = checkout_page.get_item_price()
    tax = checkout_page.get_tax()
    total = checkout_page.get_total()

    assert item_price + tax == pytest.approx(total, abs=0.01)