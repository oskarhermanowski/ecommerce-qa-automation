from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page

        self.cart_item = page.locator(".cart_item")
        self.product_name = page.locator(".inventory_item_name")
        self.checkout_button = page.locator("#checkout")

    def checkout(self):
        self.checkout_button.click()