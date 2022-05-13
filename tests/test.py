import os
import unittest
import requests
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from app import app, db

TEST_DB = 'test.db'

class KanbanBoardTests(unittest.TestCase):
    # to execute before the test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.assertEqual(app.debug, False)
    # to execute after the test
    def tearDown(self):
        pass
    
    ## testing the main page - if opens for the user
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    ## testing the login page - if opens for the user
    def test_login_page(self):
        response = requests.get('http://127.0.0.1:5000/login')
        self.assertEqual(response.url, 'http://127.0.0.1:5000/login')

    ##testing the sign up process, whether the user is able to access Kanban Board (home) page
    def test_sign_up(self):
        user_info = {'username':'Andriy', 'password':'11userpass87', 'retype':'11userpass87'}
        response = requests.post('http://127.0.0.1:5000/signup', data = user_info)
        response = requests.post('http://127.0.0.1:5000/login', data = user_info)
        self.assertEqual(response.url, 'http://127.0.0.1:5000/login')

    ## testing if a user with correct password can log in 
    def test_correct_login(self):
        user_info = {'username':'Andriy', 'password':'11userpass87'}
        response = requests.get('http://127.0.0.1:5000/login', data = user_info)
        self.assertEqual(response.url, 'http://127.0.0.1:5000/login')

    ## testing if a user with incorrect password does not log in and remains on the starting (login) page
    def test_incorrect_login(self):
        user_info = {'username':'Andriy', 'password':'12345'}
        response = requests.post('http://127.0.0.1:5000/login', data = user_info)
        self.assertEqual(response.url, 'http://127.0.0.1:5000/login')

    # ## testing it a task can get added
    # def test_add_task(self):
    #     task_info = {'task_name': "buying a gift", 'task_status': "todo"}
    #     response = self.app.post('/update', data = task_info, follow_redirects=True)
    #     self.assertEqual(response.status_code, 200)

    # ## testing if a task can be moved
    # def test_move_task(self):
    #     self.test_add_task()
    #     response = self.app.post('/update', follow_redirects=True)
    #     self.assertEqual(response.status_code, 200)

    # ## testing if a task can be deleted
    # def test_delete_task(self):
    #     self.test_add_task()
    #     response = self.app.get('/delete', follow_redirects=True)
    #     self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
     unittest.main()import os
import unittest
import requests
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from app import app, db

TEST_DB = 'test.db'

class KanbanBoardTests(unittest.TestCase):
    # to execute before the test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.assertEqual(app.debug, False)
    # to execute after the test
    def tearDown(self):
        pass
    
    ## testing the main page - if opens for the user
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    ## testing the login page - if opens for the user
    def test_login_page(self):
        response = requests.get('http://127.0.0.1:5000/login')
        self.assertEqual(response.url, 'http://127.0.0.1:5000/login')

    ##testing the sign up process, whether the user is able to access Kanban Board (home) page
    def test_sign_up(self):
        user_info = {'username':'Andriy', 'password':'11userpass87', 'retype':'11userpass87'}
        response = requests.post('http://127.0.0.1:5000/signup', data = user_info)
        response = requests.post('http://127.0.0.1:5000/login', data = user_info)
        self.assertEqual(response.url, 'http://127.0.0.1:5000/login')

    ## testing if a user with correct password can log in 
    def test_correct_login(self):
        user_info = {'username':'Andriy', 'password':'11userpass87'}
        response = requests.get('http://127.0.0.1:5000/login', data = user_info)
        self.assertEqual(response.url, 'http://127.0.0.1:5000/login')

    ## testing if a user with incorrect password does not log in and remains on the starting (login) page
    def test_incorrect_login(self):
        user_info = {'username':'Andriy', 'password':'12345'}
        response = requests.post('http://127.0.0.1:5000/login', data = user_info)
        self.assertEqual(response.url, 'http://127.0.0.1:5000/login')

    # ## testing it a task can get added
    # def test_add_task(self):
    #     task_info = {'task_name': "buying a gift", 'task_status': "todo"}
    #     response = self.app.post('/update', data = task_info, follow_redirects=True)
    #     self.assertEqual(response.status_code, 200)

    # ## testing if a task can be moved
    # def test_move_task(self):
    #     self.test_add_task()
    #     response = self.app.post('/update', follow_redirects=True)
    #     self.assertEqual(response.status_code, 200)

    # ## testing if a task can be deleted
    # def test_delete_task(self):
    #     self.test_add_task()
    #     response = self.app.get('/delete', follow_redirects=True)
    #     self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
     unittest.main()
