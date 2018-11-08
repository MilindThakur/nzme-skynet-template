from selenium.webdriver.common.by import By
from nzme_skynet.core.controls.textinput import TextInput
from nzme_skynet.core.controls.element import Element
from nzme_skynet.core.controls.image import Image


class GoogleSearchResultsPage(object):
    # WebElements
    logo = Image(By.ID, "logo")
    searchresults = Element(By.ID, "res")
    searchresultscontent = TextInput(By.XPATH, ".//*[@id='search']/div/div/div/div[1]")





