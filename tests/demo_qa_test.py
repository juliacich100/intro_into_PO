from selene.support.shared import browser
from selene import have, be, command
import os
import tests
from model.pages import practice_form_helpers


def test_student_registration_form():
    browser.open('/automation-practice-form')
    practice_form_helpers.type_first_name('Julia')
#    browser.element('#firstName').should(be.blank).type('Julia')
    practice_form_helpers.type_last_name('Ekkart')
#    browser.element('#lastName').should(be.blank).type('Ekkart')
    practice_form_helpers.type_email('test@mail.com')
#    browser.element('#userEmail').should(be.blank).type('test@mail.com')
    practice_form_helpers.pick_female_gender()
#    browser.element('[name=gender][value=Female] + label').click()
    practice_form_helpers.type_phone_number('0123456789')
#    browser.element('#userNumber').type('0123456789')
    practice_form_helpers.select_birthday()
#    browser.element('[class = "react-datepicker__input-container"]').click()
#    browser.element('[class = "react-datepicker__month-select"]').click()
#    browser.element('[value= "10"]').click()
#    browser.element('[class = "react-datepicker__year-select"]').click()
#    browser.element('[value="1985"]').click()
#    browser.element('[class = "react-datepicker__day react-datepicker__day--014"]').click()

#    ads = browser.all('[id^=google_ads_][id$=container__]')
#    ads.should(have.size_less_than_or_equal(3))
#    ads.perform(command.js.remove)

    practice_form_helpers.choose_hobbies('Music')
#    browser.element('[for="hobbies-checkbox-3"]').click()
    practice_form_helpers.type_subject('Accounting')
#    browser.element('#subjectsInput').type('Accounting').press_enter()

    practice_form_helpers.select_picture('resources/more.jpg')

#    browser.element('#uploadPicture').set_value(
#        os.path.abspath(
#        os.path.join(os.path.dirname(tests.__file__), 'resources/more.jpg')
#        )
#    )

    practice_form_helpers.type_address('Sitsevaya st')
#    browser.element('#currentAddress').should(be.blank).type('Sitsevaya st')



#    browser.element('#sate [id^=react-select][id*=input]').type('Rajasthan').press_enter()
    practice_form_helpers.select_state('Rajasthan')
#    browser.element('#state [id*=input]').click()
#    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Rajasthan')).click()
#   browser.element('#city [id^=react-select][id*=input]').type('Jaipur').press_enter()
    practice_form_helpers.select_city('Jaipur')
#    browser.element('#city').click()
#   browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Jaipur')).click()
    practice_form_helpers.submit_data()
#    browser.element('#submit').press_enter()
    practice_form_helpers.validate_data(
        'Julia Ekkart',
        'test@mail.com',
        'Female',
        '0123456789',
        '14 November,1985',
        'Accounting',
        'Music',
        'more.jpg',
        'Sitsevaya st',
        'Rajasthan Jaipur')
#    browser.element('.table').all('td').even.should(have.texts(
#        'Julia Ekkart',
#        'test@mail.com',
#        'Female',
#        '0123456789',
#        '14 November,1985',
#        'Accounting',
#        'Music',
#        'more.jpg',
#        'Sitsevaya st',
#        'Rajasthan Jaipur'
#    ))