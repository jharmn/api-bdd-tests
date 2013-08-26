Feature: Bitly link shortener

@Positive @Oauth @Bitly @User
Scenario: Get access token
	Given I use the bitly host
	When I access the resource url "/oauth/access_token"
	And I provide authentication credentials
	And I post to the url
	Then the status code should be 200
	And the results should be saved as "access_token" for later

@Positive @User @Bitly
Scenario: Get user info
	Given i use the bitly host
	When I access the resource url "/v3/user/info"
	And I provide parameter "access_token" as the value "access_token"
	And I retrieve the JSON results
	Then the status code should be 200
	And it should have the field "status_code" containing the value 200 
