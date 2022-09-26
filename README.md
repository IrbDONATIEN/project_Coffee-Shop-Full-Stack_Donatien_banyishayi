# Coffee Shop Full Stack

## Full Stack Nano - IAM Final Project

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. But they need help setting up their menu experience.

You have been called on to demonstrate your newly learned skills to create a full stack drink menu application. The application must:

1. Display graphics representing the ratios of ingredients in each drink.
2. Allow public users to view drink names and graphics.
3. Allow the shop baristas to see the recipe information.
4. Allow the shop managers to create new drinks and edit existing drinks.

This project is write in Python/Flask and SQLITE database system.


## Auth0 Account:
> A)- Then update the information in a file auth.py
 ```
AUTH0_DOMAIN = AUTH0_DOMAIN
ALGORITHMS = ALGORITHMS
API_AUDIENCE = API_AUTH0_AUDIENCE
 ```
> B)- I have created two dummy accounts on my Auth0 profile, both of them are verified and functional.
 
 #### Manager Account
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFmRU9CWFdLeWJiSmd4UEljUU9LNiJ9.eyJpc3MiOiJodHRwczovL2RvbmF0aWVuYmFueWlzaGF5aTIudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYzMmY0YjFkODhjYjU3ZTFmZDhlNjEyYyIsImF1ZCI6InNob3Bjb2ZmZWUiLCJpYXQiOjE2NjQxMzQ3MDcsImV4cCI6MTY2NDIyMTEwNywiYXpwIjoiUWd5VENzNktNUzVqeGM0V1hERnFTbnpKdDFHZ2tWZW4iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpkcmlua3MiLCJnZXQ6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.Q3V77oeGd3NQp7CNd95oFRlXwaBPNou_zcUbjAUgj2jBJXgw_NaY1yDo1V4MW5K6wxMj8cIS1aZEq0l_E2JxQU5EVavgLro7JKy7QqFEW-cWZnfT2fRUN7VcbePT8GwiKlS6DuteVRhRebcmJQxitUePPKeQZE9Yw3kc89W-YonMUwX7fYbW4cObJemHUzsuUl5O8BQPF8NIvcBX4xBzFMH46maxFKsomDs4TuseRpVlY0ayoS8xctzRdH3BUjKJkPT-PkGblbYbo7d1z7aZzFlPVOeYQpijRsuKqdtNPZTRWJfum2mLn6YqUG0cciSOCY1hQNY0KvfBufZUsXvd-g
```

 #### Barista Account
 ```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFmRU9CWFdLeWJiSmd4UEljUU9LNiJ9.eyJpc3MiOiJodHRwczovL2RvbmF0aWVuYmFueWlzaGF5aTIudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYzMmY0YjFkODhjYjU3ZTFmZDhlNjEyYyIsImF1ZCI6InNob3Bjb2ZmZWUiLCJpYXQiOjE2NjQyMTg4MjQsImV4cCI6MTY2NDMwNTIyNCwiYXpwIjoiUWd5VENzNktNUzVqeGM0V1hERnFTbnpKdDFHZ2tWZW4iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpkcmlua3MiLCJnZXQ6ZHJpbmtzIiwiZ2V0OmRyaW5rcy1kZXRhaWwiLCJwYXRjaDpkcmlua3MiLCJwb3N0OmRyaW5rcyJdfQ.MgDwabgGwJCuO43EAmMm0Yk7rQlLbCGdSLlhj34O6-8e3knkCtKR22QY1AgYKX8MuBv5DW-p5ZR8ongLlrrefg0l_WGjnfOnFhziHaOPJU4tmUzUeSKt98zkjW7vHsuijvpHstdtYb7AEzRCRV5AOnyXeDsScdc3N16aHQg6dgw3fAeCsIOW9i57dcaB6I4sOtSwFx0_4vv2_19mE7c3lJcDNHBUcteeGOUZckpEtbFRnbMQLHCTsCZWLjX8PuEZJtkswcO2hOZFis7ZYzU7tG6C_9ARHekjAKbKUFj5r8vRGUqfh_-oCKiq0LDiH9b8u3J5UKLUhwnMSOLsNyShpg

 ```
 
 ## POSTman:
 
* Imported collection with configured tokens can be found at: /backend/udacity-fsnd-udaspicelatte.postman_collection.json
* Exported Test results containing 20 successful cases: /backend/udacity-fsnd-udaspicelatte.postman_collection_test_run.json


 ## Backend:
 
* Added Auth0 functionalities on auth.py 
* Implemented RESTful endpoints api.py
* Implemented error handlers 400, 404, 422


## Running the app:
A)- Install dependencies with

```
- pip3 install -r backend/requirements.txt
- pip install dotenv for secret informations login
- Install Postman for test API
```
B)- Running the server
From within the ./src directory first
```
- export FLASK_APP=api.py in Linux and MacOS;
- set FLASK_APP=api.py in Windows
```
C)- To run the server/app, execute
 ```
 flask run --reload
  ```

## Frontend:
* Added the Auth0 variables on environment.ts 
* Guarantee that the frontend can be launched upon an ionic serve command and the login/token retrieval are functional


#### Installing Project dependencies
* This project uses NPM to manage software dependencies. 
* NPM relies on the package.json file located in the frontend directory of this repository. 
* After cloning, open your terminal and run:
```
npm install
```

#### Running Your Frontend in Dev Mode
```
ionic serve
```

## .gitignore:
* enviornment 
* node_modeules
* .env this file contain informations critical with file settings.py


[View the README.md within ./backend for more details.](./backend/README.md)


[View the README.md within ./frontend for more details.](./frontend/README.md)

