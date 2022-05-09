from flask import Flask, render_template, request, redirect, url_for, flash, g
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user


app = Flask(__name__)
app.secret_key = 'super secret key'

login = LoginManager()
login.init_app(app)
login.login_view = 'login'

path = os.path.abspath(os.getcwd()) + '\\kanban.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path

db = SQLAlchemy(app)

class tasks(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200))
    descrip = db.Column(db.String(500))
    status = db.Column(db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))

class User(UserMixin, db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200))
    password = db.Column(db.String(200))
    task_id = db.relationship('tasks', backref='user', lazy='dynamic')

@app.route('/', methods=['GET'])
@login_required
def index():
    g.user = current_user
    todolist = []
    doinglist = []
    donelist = []
    tasklist = tasks.query.filter_by(user_id = g.user.id).all()
    for item in tasklist:
        if item.status == 'todo':
            todolist.append(item)
        elif item.status == 'doing':
            doinglist.append(item)
        elif item.status == 'done':
            donelist.append(item)
    return render_template('kanban.html', todolist=todolist, doinglist=doinglist, donelist=donelist)

@app.route('/add', methods=['POST'])
def add():
    g.user = current_user
    todo = tasks(task=request.form['todoitem'], descrip=request.form['tododescrip'], status='todo')
    todo.user = g.user
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/todoing', methods=['POST'])
def todoing():
    imd = request.form
    form = imd.to_dict()
    task_id = next(iter(form))
    task = tasks.query.filter_by(id=int(task_id)).first()
    task.status = 'doing'
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/todone', methods=['POST'])
def todone():
    imd = request.form
    form = imd.to_dict()
    task_id = next(iter(form))
    task = tasks.query.filter_by(id=int(task_id)).first()
    task.status = 'done'
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    imd = request.form
    form = imd.to_dict()
    task_id = next(iter(form))
    task = tasks.query.filter_by(id=int(task_id)).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username'], password=request.form['password']).first()
        if user is None:
            error = 'Invalid credentials'
            return render_template('login.html', error=error)
        login_user(user)
        return redirect(url_for('index'))
    elif request.method == 'GET':
        return render_template('login.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        new_user = User(username=request.form['username'], password=request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        flash('User successfully registered')
        return redirect(url_for('login'))
    elif request.method == 'GET':
        return render_template('signup.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    sess.init_app(app)
    app.run(debug=True)
