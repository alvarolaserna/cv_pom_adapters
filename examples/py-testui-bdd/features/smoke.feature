@Login
Feature: Test Part 1

  Background: App is opened
    Given I am in landing page
    And I Accept Cookies

@RightCreds
  Scenario: Login with right credentials
    Given I click on Contact us
    And I put data: Alvaro Laserna and alvaro.lasernalopez@testdevlab.com
