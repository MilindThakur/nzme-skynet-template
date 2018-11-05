from nzme_skynet.core.controls.button import Button
from nzme_skynet.core.controls.textinput import TextInput
from nzme_skynet.core.pageobject.basewebpage import BaseWebPage
from selenium.webdriver.common.by import By

class SearchComponent(BaseWebPage):
    inputsearch = TextInput(By.ID, 'search-input')
    searchbutton = Button(By.CSS_SELECTOR, '.search-submit')

    def enter_search_terms(self, searchterms, date, people, mealtime):
        if not self.inputsearch.is_currently_visible():
            raise Exception("Search was not visible on screen")
        if searchterms is not None:
            self.inputsearch.set_value(searchterms)
        elif len(self.inputsearch.value) > 0:
            self.inputsearch.clear()
        if people is not None:
            self.noofpeople.select_by_index(people)
        if mealtime is not None:
            self.mealtime.select_by_value(mealtime)

    def search_for(self, searchterms=None, date=None, people=None, mealtime=None):
        self.enter_search_terms(searchterms, date, people, mealtime)
        self.searchbutton.click()

