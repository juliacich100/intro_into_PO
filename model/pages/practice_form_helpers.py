from selene.support.shared import browser
from selene import be, have
from model.elements import dropdown, datepickers, radiobuttons, checkboxes
from model.utils import paths


def type_first_name(value):
    browser.element('#firstName').should(be.blank).type(value)


def type_last_name(value):
    browser.element('#lastName').should(be.blank).type(value)


def type_email(value):
    browser.element('#userEmail').should(be.blank).type(value)


def pick_female_gender():
    radiobuttons.select_option('[name=gender][value=Female] + label')


def type_phone_number(value):
    browser.element('#userNumber').type(value)


def select_birthday():
    datepickers.select_date_of_birth()


def choose_hobbies(value):
    checkboxes.select_options('[for^=hobbies-checkbox]', value)


def type_subject(name):
    browser.element('#subjectsInput').type(name).press_enter()


def select_picture(rel_path):
    paths.path_to_image('#uploadPicture', rel_path)


def type_address(text):
    browser.element('#currentAddress').should(be.blank).type(text)


def select_state(value):
    dropdown.select_option('#state', value)


def select_city(value):
    dropdown.select_option('#city', value)


def submit_data():
    browser.element('#submit').press_enter()


def validate_data(*values):
    browser.element('.table').all('td').even.should(have.texts(values))