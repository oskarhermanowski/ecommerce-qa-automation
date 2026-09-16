from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_product_is_visible_in_cart(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)

    # Add product
    inventory_page.add_backpack_to_cart()

    # Open Cart
    inventory_page.open_cart()

    # Verify product
    expect(cart_page.cart_item).to_have_count(1)
    expect(cart_page.product_name).to_have_text("Sauce Labs Backpack")

def test_remove_product_from_cart(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    expect(cart_page.cart_item).to_have_count(1)

    cart_page.remove_backpack()

    expect(cart_page.cart_item).to_have_count(0)

def test_continue_shopping_from_cart(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    cart_page.continue_shopping()

    expect(logged_in_page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(inventory_page.page_title).to_have_text("Products")

def test_add_multiple_products_to_cart(logged_in_page: Page):
    inventory_page = InventoryPage(logged_in_page)
    cart_page = CartPage(logged_in_page)

    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()

    expect(inventory_page.cart_badge).to_have_text("2")

    inventory_page.open_cart()

    expect(cart_page.cart_item).to_have_count(2)