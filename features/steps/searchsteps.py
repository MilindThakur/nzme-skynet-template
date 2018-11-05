from behave import *
from pages.pageobject.rhbasepage import RhBasePage
from pages.pageobject.search.searchresultspage import SearchResultsPage

use_step_matcher("re")

@when('I search on restaurant hub for "(?P<searchterm>.+)"')
def i_search_on_restaurant_hub_for_the_city(context, searchterm):
    context.homepage = RhBasePage()
    context.searchterm = searchterm  # Used in later steps
    context.homepage.search.search_for(searchterms=searchterm)


@then('I can see "(?P<expected>.+)" in the search results')
def i_see_the_suggested_search_results(context, expected):
    assert SearchResultsPage().get_search_result_by_restaurant_name(expected)
