# Created by kumar at 5/11/18

    ##### This feature file contains a sample feature and a scenario for testing a web application#####

Feature: Search for specific websites on google
  As a user of internet
  I want to search for Restaurant Hub website on google
  So that I can explore Restaurant Hub website

  @google @search
  Scenario: Search on google for Restaurant Hub
    Given I am on the google homepage
    When I search on google for "Restaurant Hub"
    Then I can see "Restaurant Hub" in search results