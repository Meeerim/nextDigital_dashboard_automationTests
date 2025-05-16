from playwright.sync_api import expect
from pages.base_page import BasePage
import re


class LoginPage(BasePage):
    def open(self):
        self.page.goto("https://nextdigital.it.com/")
        self.page.get_by_role("link", name="Login").click()
        expect(self.page).to_have_url("https://nextdigital.it.com/signin")

    def login(self, email, password):
        self.page.get_by_role("textbox", name="Email Id").fill(email)

        self.page.get_by_role("textbox", name="Password").fill("naz")
        self.page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()

        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Sign in").click()

    def login_with_google(self):
        self.page.get_by_role("button", name="Continue with Google").click()

    def forgot_password(self):
        self.page.get_by_role("link", name="Forgot Password?").click()
        self.page.get_by_role("textbox", name="Email Address").click()
        self.page.get_by_role("textbox", name="Email Address").fill("skmeerim@gmail.com")
        self.page.get_by_role("button", name="Send Reset Link").click()

    def verify_forgot_password(self):
        self.page.get_by_role("button", name="Back to Reset Password").click()
