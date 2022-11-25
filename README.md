<h1 align="center"> Project Assets Tracker </h1><br>
<h6 align="Center">

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
 [![git](https://badgen.net/badge/icon/git?icon=git&label)](https://git-scm.com) [![Visual Studio](https://badgen.net/badge/icon/visualstudio?icon=visualstudio&label)](https://visualstudio.microsoft.com)

</h6>

<br>

<h4 align="center">
<a href="https://github.com/yeazin/assets-tracker#-project-installation-"> Project Installation</a> | 
<a href="https://github.com/yeazin/assets-tracker#project-flow"> Project Flow </a>
|<a href="https://github.com/yeazin/assets-tracker#-project-documention-"> Project Documention </a>

</h4> 

<br>


<h2 align="center"> Project Installation </h2>
<br>

#### Clone the repository using the following command

```bash
git clone https://github.com/yeazin/assets-tracker.git
# After cloning, move into the directory 
# having the project files 
```
#### Create a virtual environment where all the required python packages will be installed

```bash
# Use this on Windows
python -m venv env
# Use this on Linux and Mac
python3 -m venv env
```
#### Activate the virtual environment

```bash

# Windows
env\Scripts\activate.bat

# Linux and Mac
source env/bin/activate

```
#### Install all the project Requirements

```bash

pip install -r require.txt

```
#### Apply migrations and create your superuser (follow the prompts)

```bash

# Apply make migrations
python manage.py makemigrations

# apply migrations and create your database
python manage.py migrate

# Create a user with manage.py
python manage.py createsuperuser

```

#### Run the development server

```bash
# run django development server
python manage.py runserver

```
Now we are good to Go . We can check the [127.0.0.1:8000](http://127.0.0.1:8000) <br> for The root API documention.
<br>

<h2 align="center">Project Flow</h2>
<br>


#### Project Structure 
<br>

```bash 


    mainConfig/  #Root Config folder
        |-- __init__.py
        |__ settings/
            |-- base.py # base settings
            |-- development # development settings)
        |__ models/
            |-- mixxin.py # Mixxin abstruct models 
        |-- urls.py (Root URL file)
        |-- wsgi.py
        |-- asgi.py


    structure   # All the APPs will be under on it
        |-- __init__.py
        |__ accounts/ 
            |-- __init.py
            |__ models/ # database folder  
                |-- base.py # Base User config
                |-- employee.py # employee models 
            |__ tests / # tests folder 
                |-- __init__.py
                |-- urls_tests.py # URLs test case
            |-- views 
            |-- serializer.py # API file
            |-- urls.py # accounts URL file)
            |-- admin.py

        |__ company/
            |-- __init__.py
            |-- models.py # Company database file
            |__ views # Views folder
                |-- company view # company views
                |-- assets view # asstes views 
            |__ tests / # tests folder 
                |-- __init__.py
                |-- urls_tests.py # URLs test case
            |-- serializer.py # API file
            |-- urls.py # Code list URL file)
            |-- admin.py

    |-- manage.py
    |-- .env  
    |-- .gitignore
    |-- db # development database 
    |-- require.txt # package dependency file
    

```
<br>

<h2 align="center"> Project Documention </h2>


#### Company Module 
<br>

```bash 

    Employee and Profiles 
        - Employee can be registered to the system by following fields
            - Full Name
            - Unique Phone Number
            - password 
            - confirm password

    Company Registration 
        - Company can be registered with their name 
        - During the Registration company will have an Admin
        - Admin can add Employee to the company
        - Validation added when duplicate employee occurs 
        - ALL CRUD operations 


```
<br>

#### Assets Tracking Module
<br>

```bash 

    Company Assets
        - Company can add assets as many as want.
        - Fields are
            - Deivice Name,Devce Type
        - All CRUD operations included 
    
    Deligate Assets to Employee
        - Admin of the company can assign asset to any employee
        - Log will be saved when assets are checking out and return.
        - Date and time will be saved 
        - Log Message can be added 

```
<br>


#### Tracking Assets Module 
<br>

```bash 

    - All assets log can be viewed by the admin of the company. 
    - Single Asset log can be also viewed by the admin 
    - In a single assets the following fields will be shown 
        - Company Name 
        - Asset name 
        - Asset Type
        - Employee Name
        - Asset checking out date 
        - Asset checking out condition Log 
        - Asset return date 
        - Asset return condition log 


```
<br>

#### Test Case 
<br>

```bash 

    All the URLs TestCase is inclued in each app testing folder

```

#### Thanks for Tagging alone with the  Documention 

Wish you a Great Time ...

If you have any quiry regarding this project <br>
Feel free to contact me :

Email : naz.yeasin@gmail.com