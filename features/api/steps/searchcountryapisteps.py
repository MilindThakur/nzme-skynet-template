from behave import *
from api.searchcountry.searchcountryapi import SearchCountryApi

use_step_matcher("re")

@given("I call search country api with the country code NZ")
def step_impl(context):
    context.api_response = SearchCountryApi().get()

@then("I should receive an authorized response")
def step_impl(context):
    assert context.api_response is not None
    assert context.api_response.status_code == 200, 'Received http code {} instead'.format(context.api_response.status_code)