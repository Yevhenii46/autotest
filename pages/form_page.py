import os
import time

from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators

class FormPage(BasePage):

    def fill_fields_and_submit(self):
       person = generated_person()
       path = generated_file()
       self.remove_footer()
       self.element_is_visible(Locators.first_name).send_keys(person.first_name)
       self.element_is_visible(Locators.last_name).send_keys(person.last_name)
       self.element_is_visible(Locators.email).send_keys(person.email)
       self.element_is_visible(Locators.gender).click()
       self.element_is_visible(Locators.mobile).send_keys(person.mobile)
       subject = self.element_is_visible(Locators.subjects)
       subject.send_keys(person.subject)
       subject.send_keys(Keys.RETURN)
       self.element_is_visible(Locators.hobbies).click()
       self.element_is_visible(Locators.upload_file).send_keys(path)
       os.remove(path)
       self.element_is_visible(Locators.current_address).send_keys(person.current_address)
       self.element_is_visible(Locators.submit).click()
       time.sleep(5)
       return person

    def form_result(self):
        result_list = self.elements_are_visible(Locators.result_table)
        result_text = []
        for i in result_list:
            result_text.append(i.text)

        return result_text