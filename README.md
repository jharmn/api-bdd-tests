bdd-api-lettuce
==

An example of testing an HTTP-based API using the BDD style

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
