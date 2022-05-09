import unittest
import requests
from requests import Session

class TestKanbanRequests(unittest.TestCase):

    def test_home_login(self):
        '''
        Tests that the kanban loads to login page if not logged in
        '''
        req = requests.get('http://localhost:5000/')
        self.assertEqual(req.url, 'http://localhost:5000/login?next=%2F')

    def test_real_login(self):
        '''
        Tests that login returns to user kanban board with known login credentials
        '''
        details = {'username':'Isaac', 'password':'407best'}
        req = requests.post('http://localhost:5000/login', data = details)

        self.assertEqual(req.url, "http://localhost:5000/")

    def test_logout(self):
        '''
        Logout redirects to login page
        '''
        req = requests.get('http://localhost:5000/logout')
        self.assertEqual(req.url, 'http://localhost:5000/login?next=%2F')

    def test_false_login(self):
        '''
        Tests that false credentials do not log in and remains on login page
        '''
        details = {'username':'fake', 'password':'fake'}
        req = requests.post('http://localhost:5000/login', data = details)

        self.assertEqual(req.url, 'http://localhost:5000/login')

    def test_signup(self):
        '''
        Tests that sign up takes to login page
        '''
        details = {'username':"Kalia", 'password':"superdupersecret6575"}
        req = requests.post('http://localhost:5000/signup', data = details)

        self.assertEqual(req.url, 'http://localhost:5000/login')

if __name__ == "__main__":
    unittest.main()
