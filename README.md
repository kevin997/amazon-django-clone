# Amazon Clone Django Rest Framework (ADRF) Installation - Configuration Steps


In order to make this project work in your environment, make sure you follow the following steps

This Steps assumes your are runnning a Linux distro, if you are running Windows, find out ways in which you can run this commands


***
***

## Requirements

***
***

> 1. Python [latest verion]
> 2. Virtual Environment
> 3. PostMan
> 4. Chrome Browswer
> 5. Nodejs & Npm For React


## Brancing Rules

When you clone this project, you will be by default in the ``develop`` branch.

First Switch to a feature branch you have created locally like : ``user-profiles-migration``, ``loing-api`` or ``register-api`` or ``add-product``

When you are in the feature branch, continue with the below steps


## Steps/Commands

### Step 1 : Virtual env Configuration
In this step, we will be start our project.

To do this we will need to create a virtual environment or switch to an existing one.
>Note: Python virtual env docs can be found [here](https://docs.python.org/3/tutorial/venv.html).

1) Virtual Environment - Open a terminal or enter into a directory and use the following command to create a virtual environment. 

> NB: I advice my students to have a directory called ``django_projects/``, where they create and environmennt and their django projects


```
python -m venv venv
```
Now activate the virtual environment with the following command, (Run this command to activate an existing environment).
```
# windows machine
venv\Scripts\activate.bat

#mac/linux
source venv/bin/activate
```
You will know your virtual environment is active when your terminal displays the following:
```
(venv) path\to\amazon-django-clone\
```

2) Packages and requirements - Our project will rely on a whole bunch of 3rd party packages (requirements) to function. We will be using a Python package manager to install packages throughout this course. 
I have already created a requirements.txt file. Check out requirements.txt
Let's go ahead and install our project requirements. Add the following code to you terminal.

```
pip install -r requirements.txt
```

### Step 2: Preparing to Migrate

Make sure to check your database connection details in the .env.example file
```
export MYSQL_DB_NAME='YOUR_DATABASE_NAME'
export MYSQL_DB_USER='YOUR_DB_USER'
export MYSQL_DB_KEY='YOUR_DB_SECRET'
```

4) Secrets and Environment Variables - It is good practice to separate sensitive information from your project. We have installed a package called 'python-dotenv' that helps us manage secrets easily. Lets go ahead and create a env file to store information that is specific to our working environment. Use the following command in your terminal.

```
# windows machine
copy env.template .env

#mac/linux
cp env.template .env
```

You can use your new .env file to store API keys, secret_keys, app_passwords and you will gain access to these in the Django app.
***
***

## Step 3: Exloring the Template Code 

Django application consists of project and app, it also generates an automatic base directory for the app, so we can focus on writing code (business logic) rather than creating app directories.

The difference between a project and app is, a project is a collection of configuration files and apps whereas the app is a web application which is written to perform business logic.

I thus created a app with the ``python3 manage.py startapp`` command called `core`

> You will find a folder called : amazon-django-clone/core

This folder ``core`` is the part of our project that manages simple tasks like storing contacts, marketing, informatoin about our systems, etc.

> NB: It should not be edited, you can view how the files are structured. it will help you understand how Django and the Rest framework works


## Step 4: Front-end Configuration

We are using Vite

Locate the React folder `amazon-react-app` and run the following command

``
npm install
``

The above command will install necessary packages neede to spin off the fron end

Next when the installation is done, run:

``
npm run dev
``


# Where to go from here ?

> Get back to the mentor in order to get more instructions

***
Provided By OKENLY SOLUTIONS LLC
***
