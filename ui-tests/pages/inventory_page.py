from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

        self.page_title = page.locator(".title")
        self.cart = page.locator('[data-test="shopping-cart-link"]')
        self.cart_badge = page.locator(".shopping_cart_badge")

        self.backpack_add_button = page.locator(
            "#add-to-cart-sauce-labs-backpack"
        )

    def add_backpack_to_cart(self):
        self.backpack_add_button.click()

    def open_cart(self):
        self.cart.click()