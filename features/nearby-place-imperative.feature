Feature: Geonames nearby place name 

@Positive @Get @Nearby
Scenario: Get nearby place name
	Given I use the geonames host
	When I access the resource url "/findNearbyPlaceNameJSON"
        And I provide parameter "username" as "jharmon"
        And I provide parameter "lat" as "<lat>"
        And I provide parameter "lng" as "<long>"
	And I retrieve the JSON results
	Then the status code should be 200
	And it should have a list "geonames"
	And the list should have at least 1 item
	And the list should have the field "countryId" containing the value "<countryId>"
	And the list should have the field "toponymName" containing the value "<toponymName>"
Examples:
	| lat		| long		| countryId 	| toponymName 	|
	| 30.4754724	| -98.1564068	| 6252001	| Spicewood	|
	| 34.134103	| -118.321694	| 6252001	| Universal City|
	| 48.85815	| 2.29452	| 3017382	| Paris 10 Ancien - Quartier Invalides	|

@Negative @Get @User
Scenario: Invalid username does not work
	Given I use the geonames host
	When I access the resource url "/findNearbyPlaceNameJSON"
        And I provide parameter "username" as "fdafdafdfdafda"
        And I provide parameter "lat" as "30.4754724"
        And I provide parameter "long" as "-98.1564068"
	And I retrieve the JSON results
	Then the status code should be 200
        And it should have the error "status" containing the value "user does not exist."
