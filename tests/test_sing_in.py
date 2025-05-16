from pages.login_page import LoginPage


def test_sign_in(page):
    sign_in = LoginPage(page)
    sign_in.open()
    sign_in.login("nazirasabyt@gmail.com", "nazira12345")


def test_google_sign_in(page):
    sign_in = LoginPage(page)
    sign_in.open()
    sign_in.login_with_google()


def test_forgot_password(page):
    sign_in = LoginPage(page)
    sign_in.open()
    sign_in.forgot_password()
    sign_in.verify_forgot_password()
