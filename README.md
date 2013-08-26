api-bdd-tests
==

An example of testing HTTP-based APIs using the BDD principles 

Requirements
--
* virtualenv
* pip

Add Config
--
Add 'features/config.ini' with the following contents:
```
[bitly]
username: yourusername
password: notmypassword
host = https://api-ssl.bitly.com

[geonames]
host = http://api.geonames.org
```

Install
--
```bash
 virtualenv venv
 . venv/bin/activate
 pip install -r requirements.txt
 lettuce
```
