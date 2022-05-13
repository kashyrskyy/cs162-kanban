## REFERENCES for parts of the code I wrote here:
# https://flask.palletsprojects.com/en/2.1.x/config/
# https://flask-login.readthedocs.io/en/latest/
# https://flask-dance.readthedocs.io/en/v0.9.0/quickstarts/sqla-multiuser.html

import os

from flask import Flask, render_template, redirect, request, g, session
from flask_login import LoginManager, UserMixin, login_manager, login_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy

### Defining the application directory and database file:

# Referencing the directory path; joining the directory to a database file
app_directory = os.path.dirname(os.path.abspath(__file__))
# the database file linked to the app will be called "app.db" once created
db_file = "sqlite:///{}".format(os.path.join(app_directory, "app.db"))

### Setting up Flask application:

# creating the Flask instance
app = Flask(__name__)

# setting secret key, encoding in UTF-8 because it supports many languages that the user can use in their Kanban board application
app.secret_key = "UnimaginablySecretKey".encode('utf8')

### Setting up database models:

# using Flask to choose a configuration file; referencing https://flask.palletsprojects.com/en/2.1.x/config/ tutorial.
# the database URI that should be used for the connection
app.config["SQLALCHEMY_DATABASE_URI"] = db_file

# defining database using flask_sqlalchemy -> SQLAlchemy
db = SQLAlchemy(app)

# creating classes for Tasks and the User, to be utilized for the database
class Task(db.Model):
    '''
    Enables describing a task and connecting a task to the user in the database.
    '''
    # defining the name of the table
    __tablename__ = 'Task'
    
    # setting a unique ID for the task, making it a primary key of the table
    id = db.Column(db.Integer, primary_key=True)
    # defining the task name as a column in the database 
    task_name = db.Column(db.String(150), nullable=False, primary_key=True)
    # defining the task status as a column in the database 
    task_status = db.Column(db.String(150), nullable=False)
    # defining user of the task and it is linked to a foreign key of the user id in the user table
    task_user = db.Column(db.Integer, db.ForeignKey('User.id'))

    # defining task representation
    def __repr__(self):
        return "<Your task is: {}>".format(self.task_name)

class User(db.Model, UserMixin):
    '''
    Define user names, passwords, and their tasks.
    '''
    # defining the name of the table
    __tablename__ = 'User'

    # setting a unique ID for the user, making it a primary key of the table
    id = db.Column(db.Integer, primary_key=True)
    # defining email username as a column of db
    username = db.Column(db.String(50))
    # defining password as a column of db
    password = db.Column(db.String(50))

    # defining a one-to-many relationship
    task_id = db.relationship('Task', backref='user', lazy='dynamic')

    # definiting user representation
    def __repr__(self):
        return "<Your Username is: {}>".format(self.username)

# creating a database for the application:
db.create_all()
db.session.commit()

### Setting up Login Manager:

# applying Flask's Login Manager to manage login process; references: https://flask-login.readthedocs.io/en/latest/, https://flask-dance.readthedocs.io/en/v0.9.0/quickstarts/sqla-multiuser.html.
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'kanban_board.login'
login_manager.login_message = "Please log in to access the Kanban board!"

# using user_loader to get user's information (id)
@login_manager.user_loader
def process_user(id):
    '''
    Helps process the users' info, by querying based on their ID.
    '''
    return User.query.get(int(id))

### Setting up routes for the application:

# redirecting to login page
@app.route('/', methods=['GET', 'POST'])
def view_login():
    
    '''
    Helps the user to access the login page by redirecting to it.
    '''
    
    return redirect('login')

# signing up; if password too short, or if passwords don't match - user needs to go through the sign up process again
@app.route('/signup', methods=['GET','POST'])
def signup():
    '''
    To sign up to access the application.
    '''    
    if request.method == 'POST':
        ## password should by not less than 6 characters
        if len(request.form['password']) < 6:
            error = 'The password is too short! Please create a longer one.'
            return render_template('signup.html', error=error)
        ## original and retyped passwords should match
        if request.form['password'] != request.form['retype']:
            error = 'The passwords do not match. Please try again.'
            return render_template('signup.html', error=error)
        # making this user and instance of User() object
        registering_user = User(username=request.form['username'], password=request.form['password'])
        # adding the user (instance of User()) to a database, committing changes
        db.session.add(registering_user)
        db.session.commit()
        # once successful, user gets redirected to login, to input their credentials and access the application
        return redirect("/login")
    elif request.method == 'GET':
        return render_template('signup.html')

# logging into the application
@app.route('/login', methods=['GET', 'POST'])
def login():
    ''' 
    To log in the application; for a currently signed up user.
    '''
    if request.method == 'POST':
        # quering the user's information from a database
        user = User.query.filter_by(username=request.form['username'], password=request.form['password']).first()
        # if user doesn't match the existing database records - output error
        if user is None:
            error = 'Something went wrong! Please try logging in with valid email and password.'
            return render_template('login.html', error=error)
        # in successful - user logs in
        login_user(user)
        # user gets access to home page with the Kanban board
        return redirect("/kanban_board")
    elif request.method == 'GET':
        return render_template('login.html')

# logging out of the application
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    '''
    To log out the user; for a currently logged in user.
    '''
    session.pop('logged_in', None)
    return redirect('login')

# adding task; making sure only currently registered users can have access to add, move, and delete tasks
@app.route('/kanban_board', methods=["GET", "POST"])
@login_required
def add_task():
    '''
    To add tasks to the Kanban board.
    '''
    # defining a global user as current user (from flask_login package)
    g.user = current_user

    # for the start - no Error, and no tasks yet
    error = None
    all_tasks = None
    # checking for possible errors (if the tasks' names match)
    if request.form:
        if request.form.get("task_name") in [task.task_name for task in Task.query.all()]:
            error = "Kanban board has a task like this already! Try using a different task name."   
        # if no error - getting the task and adding it
        else:
            task = Task(id = 123, task_name=request.form.get("task_name"), task_status=request.form.get("task_status"), task_user = g.user.id)
            all_tasks = Task.query.all()
            # adding changes to a database, committing them
            db.session.add(task)
            db.session.commit()
        
    # querying and sorting all of the tasks
    all_tasks = Task.query.filter_by(task_user=g.user.id).all()

    # querying and sorting the tasks based on status
    tasks_to_do = Task.query.filter_by(task_status='todo',task_user=g.user.id).all()
    tasks_doing = Task.query.filter_by(task_status='doing',task_user=g.user.id).all()
    tasks_done = Task.query.filter_by(task_status='done',task_user=g.user.id).all()

    # returning the page with updated information after the task is added (the html page template gets rendered)
    return render_template("kanban_board.html", error=error, all_tasks=all_tasks, tasks_todo=tasks_to_do, tasks_doing=tasks_doing, tasks_done=tasks_done, myuser=current_user)

# deleting the task 
@app.route("/delete", methods=["POST"])
def delete_task():
    '''
    To delete the task from the Kanban board.
    '''
    # getting the task name from the form
    task_name = request.form.get("task_name")
    task = Task.query.filter_by(task_name = task_name).first()
    # deleting the task from the database and committing change
    db.session.delete(task)
    db.session.commit()
    # once deleted - redirect back to home page of Kanban board
    return redirect("/kanban_board")

# moving task up a level, updating the status of the task
@app.route("/update", methods=["POST"])
def move_task():
    '''
    To move the task to another column in the Kanban board.
    '''
    # getting task title and the status it is aiming to be updated with
    updated_status = request.form.get("updated_status")
    task_title = request.form.get("task_title")
    task = Task.query.filter_by(task_name=task_title).first()
    # updating task status
    task.task_status = updated_status
    # committing the change of task's status to a database
    db.session.commit()
    # once task is moved - user is redirected to at the same home page
    return redirect("/kanban_board")

# a command to run the application in Flask -> app.run(); enabling the debug to run 
if __name__ == "__main__":
    app.run(debug=True)
