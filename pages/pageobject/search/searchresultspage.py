from nzme_skynet.core.controls.clickable import Clickable
from selenium.webdriver.common.by import By
from pages.componentobject.search.resultitem import ResultItem
from pages.pageobject.rhbasepage import RhBasePage


class SearchResultsPage(RhBasePage):
    searchresults = Clickable(By.ID, "search_results")

    def get_search_result_by_restaurant_name(self, restaurant_name):
        for search_item in self.searchresults.find_sub_elements(By.CLASS_NAME, 'row'):
            item = ResultItem(search_item)
            if item.restaurantname.text == restaurant_name:
                return item
        return None