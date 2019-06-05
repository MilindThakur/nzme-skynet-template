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
    context.homepage.search.search_for(searchterm)


@then('I can see "(?P<expected_url>.+)" at the top of the results')
def step_impl(context, expected_url):
    assert GoogleSearchResultsPage().search_result_container.is_currently_visible()
    first_result_url = GoogleSearchResultsPage().get_result_url(1)
    assert expected_url in first_result_url, "Unexpected {0} found in first result".format(first_result_url)