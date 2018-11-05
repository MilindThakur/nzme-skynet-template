# Created by kumar at 5/11/18

    ##### This feature file contains a sample feature and few sample scenarios for understanding purpose #####

Feature: Search for a restaurant on Restaurant Hub
  As a user of RH
  I want to search for a restaurant of my choice on Restaurant Hub website
  So that I can book a table in the restaurant

  Background: A user navigated to RH page
    Given I am on the restaurant hub homepage

  @restaurant @search
  Scenario: Can search for listed restaurants by Restaurant name
    When I search on restaurant hub for "TestNZ2"
    Then I can see "TestNZ2" in the search results

  @location @search
  Scenario: Can search for restaurants by Location
    When I search on restaurant hub for "Kingsland"
    Then I can see "Citizen Park" in the search results

  @cuisine @search
  Scenario: Can search for restaurants by Cuisine
    When I search on restaurant hub for "Irish"
    Then I can see "The Claddagh" in the search results
