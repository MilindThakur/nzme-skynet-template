from selenium.webdriver.common.by import By
from nzme_skynet.core.controls.textinput import TextInput
from nzme_skynet.core.controls.element import Element
from nzme_skynet.core.controls.image import Image


class GoogleSearchResultsPage(object):

    logo = Image(By.ID, "logo")
    search_result_container = Element(By.ID, 'rso')

    def get_result_url(self, index):
        return self.search_result_container.find_sub_elements(By.TAG_NAME, "cite")[index-1].text
