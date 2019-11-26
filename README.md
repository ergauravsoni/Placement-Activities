# Placement-Activities
This DBMS mini project is developed using Django(Python) and PostgreSQL as RDBMS.

Steps to run the project in Windows:
1. Install python in your system.
2. Install PostgreSQL in your system.
3. Create a database named as "pmt_act" using PgAdmin.
4. Create a virtual environment in the master directory by using following command in command prompt:
  python -m venv pa_env
  (here pa_env is the name of virtual environment which i used...you may use your own name. )
5. Activate the virtual environment by:
  pa_env\Scripts\activate
6. Download all the required modules and dependencies of the project using:
  pip install <module-name>
  (Don't use angular brackets.)
7. All the required dependencies can be viewed in requirements.txt.
  (For example: First you should install django package:- pip install django)
8. After installing all the required modules issue migrations for creating database:
  python manage.py makemigrations pmt_act;
  python manage.py migrate
9. Check whether database is created in PgAdmin by refreshing.
10. After the database is created you can run the server by issuing this command:
   python manage.py runserver
11. Open localhost:8000 in your browser to start the app with index page.

Thank You!!!
For further queries contact the owner of this repo.
Enjoy!!
Happy Coding.
