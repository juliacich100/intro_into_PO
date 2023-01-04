from selene.support.shared import browser


def select_date_of_birth():
    browser.element('[class = "react-datepicker__input-container"]').click()
    browser.element('[class = "react-datepicker__month-select"]').click()
    browser.element('[value= "10"]').click()
    browser.element('[class = "react-datepicker__year-select"]').click()
    browser.element('[value="1985"]').click()
    browser.element('[class = "react-datepicker__day react-datepicker__day--014"]').click()