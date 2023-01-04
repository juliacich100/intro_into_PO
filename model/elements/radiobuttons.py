from selene.support.shared import browser


def select_option(selector):
    browser.element(selector).click()