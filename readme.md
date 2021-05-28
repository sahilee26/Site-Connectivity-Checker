# Site Connectivity Checker


## Project Goal
The main objective of this project is to check the status of sites. 


## Features
* We  can add commands to allow users to add and remove sites from the list of sites to be checked.(Done)
* The users should also be able to start the tool, stop it, and determine the intervals(Done)
* In case of stop pinging URL leave interval field empty

## Different Endpoints
1. /admin: This allows user to login with the admin credentials and manage the project. The user can view the tables of the database and can also edit them directly in the provided interface.

2. /insights: This endpoint shows results fetched while pinging queries in paginated form


## Running the Project Locally
1. First, clone the repository to your local machine:
  ```bash
  git clone https://github.com/sahilee26/Site-Connectivity-Checker.git
 ```
2. Change the current directory to the project directory
  ```bash
  cd Site-Connectivity-Checker
   ```
3. Install required dependencies
```bash
  pip install requirements.txt
 ```
4. Finally run the deployment server using
```bash
  python manage.py runserver
   ```
The project will be available at 127.0.0.1:8000.



## Demonstration
![](ping.gif)
