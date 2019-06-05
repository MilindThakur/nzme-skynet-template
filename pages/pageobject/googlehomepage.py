from nzme_skynet.core.pageobject.basewebpage import BaseWebPage
from nzme_skynet.core.utils.component import Component

from pages.componentobject.search.search import SearchComponent


class GoogleHomePage(BaseWebPage):
    page_url = ''

    @Component
    def search(self):
        self._search = SearchComponent()
