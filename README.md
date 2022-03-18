# HotBox users API using JSON Web Token as client based session authentication

## install python if not already installed
## cd into the directory containing `manage.py`
## install dependencies contained in the requirements.txt
## make migrations
## migrate to database
## runserver

## JSON (body) is required for consumption of the API
##  route       -         for                     -          api-keys               -       http method

/register   -   for sign up                   -   (name, email, password)       -       POST
/login      -   authenticate user  s          -   (email, password)             -       POST
/user       -   signed in user details        -   Not required                  -       GET
/users      -   signed in user details        -   Not required                  -       GET
/logout     -   deauthenticate signed in user -   Not required                  -       POST