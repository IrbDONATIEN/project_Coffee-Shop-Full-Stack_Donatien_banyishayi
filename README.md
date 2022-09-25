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
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjFmRU9CWFdLeWJiSmd4UEljUU9LNiJ9.eyJpc3MiOiJodHRwczovL2RvbmF0aWVuYmFueWlzaGF5aTIudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYzMmY0YjQ2OGYyNmI0NWMzNTM1MThlMyIsImF1ZCI6InNob3Bjb2ZmZWUiLCJpYXQiOjE2NjQxMzQ2NjEsImV4cCI6MTY2NDIyMTA2MSwiYXpwIjoiUWd5VENzNktNUzVqeGM0V1hERnFTbnpKdDFHZ2tWZW4iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpkcmlua3MiLCJnZXQ6ZHJpbmtzLWRldGFpbCJdfQ.L_e_NsyDlH1oq1Ln1nxO6vvAIrVRlYGoyMurzgLeNln1ZLIhTWmGrxXb03Wsw11mj-VKOptQbFVHSp17rR4k-katQ5WmNj8nMN7y_oumlJiSrGykoStQMrox0fihcsxjOpNt60HTKmGEvsocOY0R-sJFNK_mbjf-rmqSCo_MpBeMKb52gTb2K7mN0L-wWH1G6xTSWYsy2n3k8i1FM5QI_iJZ1ofQ6ggCDxGhiyd-d3tGYASUuOm502j2Gp0BxkoVhQnX31fk-WdTSgYnXArxlZQX-B-pGRGOPxjPy2sa0S0KQWnSeaEzOwm_fE8jt3c601gIpxHjtym4Whj-02y6r

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

