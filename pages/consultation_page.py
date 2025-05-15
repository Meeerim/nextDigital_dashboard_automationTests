# pages/consultation_page.py
import random
from playwright.sync_api import expect
from pages.base_page import BasePage


class ConsultationPage(BasePage):
    def open(self):
        self.page.goto("https://nextdigital.it.com/")
        self.page.get_by_role("link", name="Schedule Consultation").click()

    def fill_form(self, first_name, last_name, email, notes):
        self.page.get_by_role("textbox", name="First name *").fill(first_name)
        self.page.get_by_role("textbox", name="Last name *").fill(last_name)
        self.page.get_by_role("textbox", name="Email *").fill(email)

        self.page.get_by_role("textbox", name="Select a date").click()
        self.select_random_date_and_time()
        self.page.get_by_role("textbox", name="Additional Notes").fill(notes)
        self.page.get_by_role("button", name="Book Appointment").click()

    def select_random_date_and_time(self):
        self.page.get_by_role("textbox", name="Select a date").click()
        self.page.wait_for_selector('.react-datepicker__day[aria-disabled="false"]', timeout=5000)
        available_dates = self.page.query_selector_all('.react-datepicker__day[aria-disabled="false"]')
        if not available_dates:
            raise Exception("No available dates found")
        random_date = random.choice(available_dates)
        random_date.click()
        self.page.wait_for_timeout(500)

        time_slots = self.page.query_selector_all('.time-slot')
        if not time_slots:
            raise Exception("No time slots found")

        random.choice(time_slots).click()

    def verify_success(self):
        success_message = self.page.get_by_text("Booking successful! Check")
        expect(success_message).to_be_visible(timeout=10000)
