import os

from selene import have
from selene.support.shared import browser


def test_practice_form():
    browser.open('/automation-practice-form')
    browser.should(have.title('ToolsQA'))
    browser.element('[id="firstName"]').type('First name')
    browser.element('[id="lastName"]').type('Last name')
    browser.element('[id="userEmail"]').type('name@example.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[id="userNumber"]').type('799988822211')
    browser.element('[id="dateOfBirthInput"]').clear().type('01.01.1990').press_enter()
    browser.element('[id="subjectsInput"]').type('English').press_enter()
    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath('image/picture.jpeg'))
    browser.element('[id ="currentAddress"]').type('Address')
    browser.element('[id="react-select-3-input"]').type('ncr').press_enter()
    browser.element('[id="react-select-4-input"]').type('gur').press_enter()
    browser.element('[id="submit"]').press_enter()
    browser.element('[class="modal-title h4"]').should(have.text('Thanks for submitting the form'))
