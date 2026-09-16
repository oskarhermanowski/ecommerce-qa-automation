from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")

        self.complete_header = page.locator(".complete-header")
        self.error_message = page.locator('[data-test="error"]')

        self.item_price = page.locator('[data-test="inventory-item-price"]')
        self.subtotal = page.locator('[data-test="subtotal-label"]')
        self.tax = page.locator('[data-test="tax-label"]')
        self.total = page.locator('[data-test="total-label"]')

    def fill_customer_data(self, first_name, last_name, postal_code):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_checkout(self):
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()

    def get_item_price(self):
        text = self.item_price.text_content()
        return float(text.replace("$", ""))

    def get_tax(self):
        text = self.tax.text_content()
        return float(text.replace("Tax: ", "").replace("$", ""))

    def get_total(self):
        text = self.total.text_content()
        return float(text.replace("Total: ", "").replace("$", ""))