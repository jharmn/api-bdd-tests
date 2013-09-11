api-bdd-tests
==

An example of testing HTTP-based APIs using the BDD principles 

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
