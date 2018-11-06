from behave import *
from pages.pageobject.googlehomepage import GoogleHomePage
from pages.pageobject.search.googlesearchresultspage import GoogleSearchResultsPage

use_step_matcher("re")

@given("I am on the google homepage")
def step_impl(context):
    context.homepage = GoogleHomePage()
    context.homepage.goto()

@when('I search on google for "(?P<searchterm>.+)"')
def step_impl(context, searchterm):
    context.homepage = GoogleHomePage()
    context.homepage.search.search_for(searchterm)

@then('I can see "(?P<expected>.+)" in search results')
def step_impl(context, expected):
    assert GoogleSearchResultsPage().searchresults.is_currently_visible()
    assert GoogleSearchResultsPage().searchresultscontent.is_currently_visible()
    assert expected in GoogleSearchResultsPage().searchresultscontent.text