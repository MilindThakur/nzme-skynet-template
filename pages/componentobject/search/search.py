from nzme_skynet.core.controls.button import Button
from nzme_skynet.core.controls.textinput import TextInput
from nzme_skynet.core.pageobject.basewebpage import BaseWebPage
from selenium.webdriver.common.by import By


class SearchComponent(BaseWebPage):
    # WebElements
    searchbox = TextInput(By.ID, "lst-ib")
    searchbutton = Button(By.NAME, "btnK")

    def search_for(self, searchterm=None):
        self.searchbox.set_value(searchterm)
        self.searchbutton.click()