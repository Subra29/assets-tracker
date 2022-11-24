<h1 align="center"> Coding Pari Na </h1><br>
<p align="center"> Technical Documention </p>
<h6 align="Center">

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
 [![git](https://badgen.net/badge/icon/git?icon=git&label)](https://git-scm.com) [![Visual Studio](https://badgen.net/badge/icon/visualstudio?icon=visualstudio&label)](https://visualstudio.microsoft.com) [![HTMX - version 1.8.4](https://img.shields.io/badge/HTMX-version_1.8.4-2ea44f)](https://htmx.org/) [![Made with  - JavaScripts](https://img.shields.io/badge/Made_with_-JavaScripts-blueviolet)](https://www.javascript.com/) [![Bootstrap - 4.4.1](https://img.shields.io/badge/Bootstrap-4.4.1-ff69b4)](https://getbootstrap.com/docs/3.4/)

</h6>

<br>

<h4 align="center">
<a href="https://github.com/yeazin/Project-Coding-Pari-Na#-project-installation-"> Project Installation</a> | 
<a href="https://github.com/yeazin/Project-Coding-Pari-Na#project-flow"> Project Flow </a>
|<a href="https://github.com/yeazin/Project-Coding-Pari-Na#-project-documention-"> Project Documention </a>

</h4> 

<br>


<h2 align="center"> Project Installation </h2>
<br>

#### Clone the repository using the following command

```bash
git clone https://github.com/yeazin/Project-Coding-Pari-Na.git
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

#### Live Project INFO

<br>
"Project Coding Pari Na" will be found to test in online .

Project URL : https://yeazin.pythonanywhere.com/ <br>
Project Admin Panel URL : https://yeazin.pythonanywhere.com/admin/
<br>
```bash 
    Admin Login credentials 

    username : sadmin
    password : 123456

    NB : You Can also use the Credential to log in client side

```
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
                |-- profile.py # profile models 
            |-- views 
            |-- serializer.py # API file
            |-- urls.py # accounts URL file)
            |-- admin.py

        |__ codelist/
            |-- __init__.py
            |-- models.py # Code list database file
            |-- views 
            |-- serializer.py # API file
            |-- urls.py # Code list URL file)
            |-- admin.py

    static/ # statict folder (css,js)
        |__ css/
            |-- bootstrap.css 
        |__ js/
            |-- htmx.js
            |-- custom_js.js
            |-- search_value.js
    
    templates/ # HTML templates folder
        |__ base/ # base html folder
            |-- base.html
            |-- header.html
        |__ list/
            |-- list_create.html
            |-- single_value.html
        |__ user/
            |-- login.html
            |-- sign-up.html

    |-- manage.py
    |-- .env  
    |-- .gitignore
    |-- db # development database 
    |-- require.txt # package dependency file
    

```
<br>

<h2 align="center"> Project Documention </h2>

#### Thanks for Tagging alone with the Technical Documention , Read the [Project Documtion here](https://github.com/yeazin/Project-Coding-Pari-Na/tree/main/docs#-coding-pari-na-documention-) 

Project Documention URL :  [https://projectcodingparina.docs](https://github.com/yeazin/Project-Coding-Pari-Na/tree/main/docs#-coding-pari-na-documention-)

Wish you a Great Time ...

If you have any quiry regarding this project <br>
Feel free to contact me :

Email : naz.yeasin@gmail.com