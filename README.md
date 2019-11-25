# Awaards

This application was built by Django version 1.11 a python framework.

#### By [Stephen Mwanza](https://github.com/Steve-design)

### Description

Mzalendo Awwaards is an application that lets you post your projects for others to view and also rate them according to the given order.

## User Stories

As a user of the application i should be able to:

* Sign in to the application to start using.
* Upload my projects to the application.
* See other projects .
* Rate a project and see the overall score.

## Setup/Installation Requirements

* Install python version 3.6.
* Install Heroku that helps to deploy your application.
* Clone https://github.com/Steve-design/awwards.git
* Atleast have a computer or a laptop
* Have an internet connection
* Live app here https://mzalendo-awwaards.herokuapp.com/

* install Django

   ```$ pip install django==1.11```

* Create a virtual environment

   `$ sudo apt-get install python3.6-venv`

   ```$ python3.6 -m venv virtual```

   ```$ source virtual/bin/activate```

* Install gunicorn: (virtual)

   ```$ python3.6 -m pip install gunicorn```


## Specifications

| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Display sign up for | N/A | Display sign up form when a user visits the site |
| Create an account | Fill the sign up form and **click submit** | Create an account and profile for the user and log the user into the site |
| Display current user's profile | **Click** my profile tab | Display the current user's profile page with their posts |
| Upload a project | **Click** upload | Direct the user to a page with a form where the user can create and submit a post |
| See other users | **Click** see on feeds | Direct the user to a page where they see a list of other users |
| rate a post | **Click** heart icon | Redirect to the timeline page where the ratings count increases and the overall score is shown |


## Technologies Used

  * Python version 3.6
  * Django version 1.11
  * Bootstrap 4
  * Postgres Database
  * Postgres
  * HTML & CSS 
  * Heroku

## License

This project is licenced under the MIT License.

Copyright (c) 2019 [Stephen Mwanza](https://github.com/Steve-design)
