from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

        self.page_title = page.locator(".title")
        self.cart = page.locator('[data-test="shopping-cart-link"]')
        self.cart_badge = page.locator(".shopping_cart_badge")

        self.sort_dropdown = page.locator(".product_sort_container")
        self.product_prices = page.locator(".inventory_item_price")
        self.product_names = page.locator(".inventory_item_name")

        self.backpack_add_button = page.locator(
            "#add-to-cart-sauce-labs-backpack"
        )
        self.bike_light_add_button = page.locator(
            "#add-to-cart-sauce-labs-bike-light"
        )

    def add_backpack_to_cart(self):
        self.backpack_add_button.click()

    def add_bike_light_to_cart(self):
        self.bike_light_add_button.click()

    def open_cart(self):
        self.cart.click()

    def sort_products(self, value):
        self.sort_dropdown.select_option(value)

    def get_product_prices(self):
        prices = self.product_prices.all_text_contents()

        return [
            float(price.replace("$", ""))
            for price in prices
        ]

    def get_product_names(self):
        return self.product_names.all_text_contents()