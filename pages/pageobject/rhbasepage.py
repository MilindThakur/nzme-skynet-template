from nzme_skynet.core.controls.element import Element
from nzme_skynet.core.controls.image import Image
from nzme_skynet.core.pageobject.basewebpage import BaseWebPage
from selenium.webdriver.common.by import By
from pages.componentobject.search.search import SearchComponent


class RhBasePage(BaseWebPage):
    logo = Image(By.CLASS_NAME, "logo-header")
    pagecontent = Element(By.CSS_SELECTOR, ".page-content.tile-grid")
    page_url = ''

    def __init__(self):
        self._search = None  # type: SearchComponent
        self._subscribe = None  # type: SubscribeComponent

    @property
    def search(self):
        if self._search is None:
            self._search = SearchComponent()
        return self._search
