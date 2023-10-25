Feature: Validate the login feature

Background:
    Given Launch the browser
    When Open the https://play.watch.tv.br/login/ website
    Then The login portal has been opened


@valid_login
Scenario: Login and play movie
    And Provide the username "sakataalan@yahoo.com.br" and password "ytXX77R@R0ByT4C#"
    And Take screenshot
    And Click on the Login button
    And Select test profile
    And Take screenshot
    And Select movie
    And Take screenshot
    And Play Movie
    And Take screenshot
    And Go to previous page
    And Take screenshot
    And Logout
    And Take screenshot
    And The login portal has been opened
    And Take screenshot
    Then Close the browser

Scenario Outline: Login with invalid credentials
    And Provide the username "<username>" and password "<password> "
    And Take screenshot
    And Click on the Login button
    And Login is failed and invalid credential error is displayed
    And Take screenshot
    Then Close the browser
    Examples:
        | username          | password          |
        | abcd@test.com     | 1234              |
        | 1234              | afsdf@test.com    |

Scenario: Login with empty username
    And Provide the password "ytXX77R@R0ByT4C#"
    And Click on the Login button
    And Login is failed and disable button is displayed
    And Take screenshot
    Then Close the browser

Scenario: Login with empty password
    And Provide the username "sakataalan@yahoo.com.br"
    And Click on the Login button
    And Login is failed and disable button is displayed
    And Take screenshot
    Then Close the browser
  


