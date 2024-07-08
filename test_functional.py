from conftest import test_setup
import pytest
import constants
from selenium.webdriver.support.ui import Select
import time
import os
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import actions
from selenium.webdriver.support.ui import Select

@pytest.mark.usefixtures("test_setup")
class Test_functional_tests():

    def get_base(self):
        # this is the getter method of the base
        base = actions.BasePage(self.driver, self.wait)
        return base

    def test_open_website_testcase1(self):
        self.driver.get(constants.URL)
        assert self.driver.title == constants.WEBSITE_NAME

    def test_search_testcase2(self):
        base= self.get_base()
        base.presence_of_elem((By.XPATH,"//input[@id='searchInput']")).send_keys(constants.SEARCH_FOR)
        base.elem_clickable((By.XPATH,"//i[@data-jsl10n='search-input-button']")).click()
        assert (self.driver.title).startswith(constants.SEARCH_FOR)

    def test_search_app_testcase3(self):
        base = self.get_base()
        text_head= base.presence_of_elem((By.XPATH,"//*[@class='mw-page-title-main']")).text
        assert text_head == constants.SEARCH_FOR

    def test_lang_change_testcase_additional(self):    #additional testcase
        base= self.get_base()
        self.driver.back()
        base.presence_of_elem((By.XPATH,"//input[@id='searchInput']")).clear()
        dropdown= base.presence_of_elem((By.XPATH,"//select[@id='searchLanguage']"))
        act= Select(dropdown)
        act.select_by_visible_text("Español")

    def test_lang_change_testcase4(self):
        base= self.get_base()
        base.presence_of_elem((By.XPATH,"//strong[normalize-space()='Español']")).click()
        assert self.driver.title == "Wikipedia, la enciclopedia libre"

    def test_todays_article_testcase5(self):
        base=self.get_base()
        self.driver.back()
        base.presence_of_elem((By.XPATH,"//strong[normalize-space()='English']")).click()
        textcheck= base.presence_of_elem((By.XPATH,"//div[@lang='en']//div//div//h2//span[2]")).text
        assert textcheck == "From today's featured article"

    def test_search_suggestions_testcase6(self):
        base=self.get_base()
        base.presence_of_elem((By.XPATH,"//input[@placeholder='Search Wikipedia']")).send_keys("Python")
        suggestions = base.presence_of_all_elems((By.XPATH,"//div[@class='cdx-menu cdx-menu--has-footer cdx-typeahead-search__menu']//li"))
        assert len(suggestions) >2

    def test_search_elem_testcase7(self):
        #Bug
        base=self.get_base()
        base.presence_of_elem((By.XPATH,"//input[@placeholder='Search Wikipedia']")).clear()
        base.presence_of_elem((By.XPATH, "//input[@placeholder='Search Wikipedia']")).send_keys(constants.KEY_SEARCH)
        base.elem_clickable((By.XPATH,"//button[@class='cdx-button cdx-button--action-default cdx-button--weight-normal cdx-button--size-medium cdx-button--framed cdx-search-input__end-button']")).click()
        assert self.driver.title == constants.KEY_SEARCH