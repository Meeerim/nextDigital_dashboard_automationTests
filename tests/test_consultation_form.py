from pages.consultation_page import ConsultationPage


def test_consultation_form(page):
    consultation = ConsultationPage(page)
    consultation.open()
    consultation.fill_form(
        first_name="mary",
        last_name="lastly",
        email="skmeerim1999@gmail.com",
        notes="i would like to create fitness app"
    )
    consultation.verify_success()