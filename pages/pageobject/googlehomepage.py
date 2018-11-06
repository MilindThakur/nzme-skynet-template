import logging
from selenium.webdriver.common.by import By
from nzme_skynet.core.controls.textinput import TextInput
from nzme_skynet.core.controls.button import Button
from nzme_skynet.core.controls.image import Image
from nzme_skynet.core.pageobject.basewebpage import BaseWebPage
from pages.componentobject.search.search import SearchComponent


class GoogleHomePage(BaseWebPage):
    page_url = ''

    def __init__(self):
        self._search = None  # type: SearchComponent

    @property
    def search(self):
        if self._search is None:
            self._search = SearchComponent()
        return self._search