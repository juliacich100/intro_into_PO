from selene.support.shared import browser
from selene import have


def select_options(selector, value):
    browser.all(selector).element_by(have.text(value)).click()