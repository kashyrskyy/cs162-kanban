# CS162 Web App Assignment - Andriy Kashyrskyy

## Application Description

The Kanban Board helps you get around you day by managing your day-to-day list of tasks to be completed. 

## Application Features

[picture here]

Feature 1.

Feature 2.

Feature 3.

## Initial Installation
Please run the code commands below in the Terminal of your code reader (e.g. Visual Studio Code) to get started. 

Note: Make sure you have opened the folder with this project by clicking "Open..." on the home page of a code reader like Visual Studio Code. Please do so before running the commands below, otherwise they will output an error.

#### For MacOS:
```
python3.6 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3.6 app.py
```

#### For Windows:
```
python3.6 -m venv venv
venv\Scripts\activate.bat
pip3 install -r requirements.txt
python3.6 app.py
```

## Setting up the Flask Application

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
