from conftest import test_setup
import pytest
import constants
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

    def test_open_website(self):
        self.driver.get(constants.URL)
        assert self.driver.title == constants.WEBSITE_NAME
