from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page

        self.cart_item = page.locator(".cart_item")

        self.product_name = (
            page.locator(".cart_item")
            .filter(has_text="Sauce Labs Backpack")
            .locator(".inventory_item_name")
)

        self.remove_backpack_button = page.locator(
            '[data-test="remove-sauce-labs-backpack"]'
)

        self.continue_shopping_button = page.locator(
            '[data-test="continue-shopping"]'
)

        self.checkout_button = page.locator('[data-test="checkout"]')

    def remove_backpack(self):
        self.remove_backpack_button.click()


    def continue_shopping(self):
        self.continue_shopping_button.click()

    def checkout(self):
        self.checkout_button.click()