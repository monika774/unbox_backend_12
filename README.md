Project setup steps:-


1 create virtual environment :-   python -m venv venv
                                venv/Scripts/activate

Adde database in mysql :-
                     DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'SpeedDataDB',  # this db name 
		'USER': 'root',
		'PASSWORD': 'root',
		'HOST':'localhost',
		'PORT':'3306',
	}
}



2. run migrations command :-
3. python manage.py makemigrations  (this  command creating for migrations in app)
4. . python manage.py migrate (this  command creating database)

5. command for creating admin:
6. python manage.py createsuperuser
7. admin :- XXXXXXXXX
8. gmail:- XXXXXXXXXXXX
9. password :- XXXXXXXXXXXXX
10. confirm password :- XXXXXXXX

11. (my admin  application : admin- speed and password - spped )
12. 
   

run server command :- python manage.py runserver

6.  
