# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from nzme_skynet.core.pageobject.basepage import BasePage


class ResultItem(BasePage):

    def __init__(self, webelement):
        super(ResultItem, self).__init__()
        self.resultitem = webelement

    @property
    def restaurantname(self):
        return self.resultitem.find_element(By.CSS_SELECTOR, 'a[data-gtm-lab=Name]')
