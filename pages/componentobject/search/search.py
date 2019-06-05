from nzme_skynet.core.controls.button import Button
from nzme_skynet.core.controls.textinput import TextInput
from nzme_skynet.core.pageobject.basewebpage import BaseWebPage
from selenium.webdriver.common.by import By


class SearchComponent(object):
    # WebElements
    searchbox = TextInput(By.NAME, 'q')
    searchbutton = Button(By.NAME, "btnK")

    def search_for(self, searchterm):
        self.searchbox.set_value(searchterm)
        self.searchbutton.click()
