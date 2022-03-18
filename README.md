# HotBox users API using JSON Web Token as client based session authentication

## install python if not already installed
## cd into the directory containing `manage.py`
## install dependencies contained in the requirements.txt
## make migrations
## migrate to database
## runserver

JSON (body) of request
##  route       -         for                    -          api-keys

### /register   -   for sign up                   -   (name, email, password)
### /login      -   authenticate user  s          -   (email, password)
### /user       -   signed in user details        -   (email, password)
### /users      -   signed in user details        -   (email, password)
### /logout     -   deauthenticate signed in user -   (Null)