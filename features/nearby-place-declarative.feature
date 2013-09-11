Feature: Geonames nearby place name

@Get @Positive @Nearby @Declarative
Scenario: Get nearby place name
	Given I use the geonames host
	When I use the "Find Nearby Place by JSON" endpoint
        And I identify my "geonames" user credentials
        And I provide coordinates 30.4754724, -98.1564068
	And I retrieve the JSON results
	Then it should have at least 1 valid "geonames" item

