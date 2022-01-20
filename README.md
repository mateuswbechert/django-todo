# django-todo

Create cards and free your mind to focus. Put your tasks on a board.

## General Info
* Developed with Python 3.8.10
* Django v4.0
* DB Adapter SQLite: does not require additional services

## Optional virtualenv
To avoid any compatibilites issues, you can use ```virtualenv``` to run the project and install dependencies. Read more on https://docs.python.org/3.8/library/venv.html

#### Quick virtualenv setup
1. Make sure you have installed ```python``` and ```pip```:
```sudo apt update && sudo apt install python3-pip```

2. Install virtualenv
```pip install virtualenv```

3. Setup a virtualenv directory
```virtualenv venv```

4. Enable the virtualenv
```source venv/bin/activate```

5. Follow to Quick start guide bellow.

* OBS: To disable the virtualenv, just run: ```deactivate```


## Quick start

1. Clone the project and navigate to directory with ```cd django-todo```

2. Install dependencies running ```pip install -r requirements.txt```

3. Run ```python manage.py migrate``` to create the polls models.

4. Start the development server running ```python manage.py runserver```

5. Visit http://127.0.0.1:8000/