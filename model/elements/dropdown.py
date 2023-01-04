from selene.support.shared import browser


def select_option(id, value):
    browser.element(id + ' [id^=react-select][id*=input]').type(value).press_enter()