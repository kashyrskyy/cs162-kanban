# CS162 Web App Assignment - Andriy Kashyrskyy

## Application Description

The Kanban Board helps you to get around your day by managing your day-to-day list of tasks to be completed. 

## Application Features

Link to a quick demo about the application - https://bit.ly/cs162-kanban-board-demo.

<img width="1440" alt="Screen Shot 2022-05-13 at 4 09 15 AM" src="https://user-images.githubusercontent.com/56770018/168237889-6c48c6d1-8ed2-4cd4-b475-85963dda133a.png">

<img width="1440" alt="Screen Shot 2022-05-13 at 4 09 50 AM" src="https://user-images.githubusercontent.com/56770018/168237949-dea78464-fa91-4b4f-9eb5-b48b360bbb4a.png">

1. **Sign Up, Log In, & Log Out**: you can authorize in the application with a username and a password that you set up. Once you log out, the changes will be saved locally in the database, thus when you log in back again - your tasks will still be there.

2. **Add a new task**: you can add a new task to your "To Do" section, which you can move up to "Doing" and "Done" Sections. 

3. **Move the tasks**: Any task can be deleted (or "erased", as this is a kind of board!). All tasks can be moved to a different priority, a level up (with the lowest level being "To Do" -> then moving to "Doing, and -> "Done").

## Initial Installation
Please run the code commands below in the Terminal of your code reader (e.g. Visual Studio Code) to get started. 

Note: Make sure you have opened the folder with this project by clicking "Open..." on the home page of a code reader like Visual Studio Code. Please do so before running the commands below, otherwise they will output an error.

#### For MacOS:
```
python3.6 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

#### For Windows:
```
python3.6 -m venv venv
venv\Scripts\activate.bat
pip3 install -r requirements.txt
```

## Setting up a database

Type the following command in your Terminal:
```
python
```
It will open a Python console, where you need to run 3 following commands, which will create a database file:
```
from app import db

db.create_all()

exit()
```
Once you exit, you should be back in your project repository.

## Setting up the Flask Application

You can use the following command:
```
python app.py
```
And you should be able to access the website locally, in your browser by opening link http://127.0.0.1:5000/.

OR 

### For MacOS:
```
export FLASK_APP=kanban.py
export FLASK_DEBUG=true
flask run
```
### For Windows:
```
set FLASK_APP=kanban.py
set FLASK_DEBUG=true
flask run
```

## Running Tests
To test the application with unit tests, please run the command below. Make sure to be in the project's root directory.

```
python3 -m unittest discover test
```
## Kanban Board Application Folder Structure

cs162-kanban-1
* [static/](./cs162-kanban-1/static)
  * [js/](./cs162-kanban-1/static/js)
    * [kanban_board.js](./cs162-kanban-1/static/js/kanban_board.js)
  * [kanban_board.css](./cs162-kanban-1/static/kanban_board.css)
  * [login.css](./cs162-kanban-1/static/login.css)
  * [signup.css](./cs162-kanban-1/static/signup.css)
* [templates/](./cs162-kanban-1/templates)
  * [kanban_board.html](./cs162-kanban-1/templates/kanban_board.html)
  * [login.html](./cs162-kanban-1/templates/login.html)
  * [signup.html](./cs162-kanban-1/templates/signup.html)
* [tests/](./cs162-kanban-1/tests)
  * [test.py](./cs162-kanban-1/tests/test.py)
* [README.md](./cs162-kanban-1/README.md)
* [app.py](./cs162-kanban-1/app.py)
* [requirements.txt](./cs162-kanban-1/requirements.txt)

\dirtree{%
  . 1 cs162-kanban-1/ .
  . 2 static/ .
  . 3 js/ .
  . 4 kanban_board.js .
  . 3 kanban_board.css .
  . 3 login.css .
  . 3 signup.css .
  . 2 templates/ .
  . 3 kanban_board.html .
  . 3 login.html .
  . 3 signup.html .
  . 2 tests/ .
  . 3 test.py .
  . 2 README.md .
  . 2 app.py .
  . 2 requirements.txt .
}
