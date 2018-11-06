# Created by kumar at 6/11/18

    ##### This feature file contains a sample feature and a scenario for testing a RESTful web-service #####

Feature: API to search country by its country code
  As an user of search country API
  I want to search a country by it's country code
  So that I can find name of the country

  Scenario: Search New Zealand by it's country code using the search country APU
    Given I call search country api with the country code NZ
    Then I should receive an authorized response
