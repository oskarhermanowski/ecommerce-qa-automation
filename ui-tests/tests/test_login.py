from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
import pytest

@pytest.mark.smoke
def test_successful_login(page: Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")


def test_login_with_invalid_password(page: Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "wrong_password")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(
        "Username and password do not match"
    )

def test_locked_out_user_cannot_login(page: Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(
        "Sorry, this user has been locked out"
    )

@pytest.mark.parametrize(
    "username,password,expected_message",
    [
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
        ("", "", "Username is required"),
    ],
)
def test_login_validation_errors(
    page: Page,
    username,
    password,
    expected_message,
):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(username, password)

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(expected_message)