from behave import *
from pages.pageobject.rhbasepage import RhBasePage

use_step_matcher("re")


@given("I am on the restaurant hub homepage")
def i_am_on_the_restaurant_hub_homepage(context):
    context.homepage = RhBasePage()
    context.homepage.goto()


