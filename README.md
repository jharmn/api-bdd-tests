api-bdd-tests
==

An example of testing HTTP-based APIs using the BDD principles.

For more info on the concepts, as well as links to BDD implementations in Groovy/CucumberJVM and .NET/Specflow: http://www.pragmaticapi.com/blog/2013/11/10/bdd-for-apis-talk-at-apistrat-sf-2013

Requirements
--
* virtualenv
* pip

Add Config
--
Add 'config.ini' with the following contents:
```
[bitly]
username = yourusername
password = notmypassword
host = https://api-ssl.bitly.com

[geonames]
host = http://api.geonames.org
username = yourusername
```

Install
--
```bash
 virtualenv venv
 . venv/bin/activate
 pip install -r requirements.txt
 lettuce
```
