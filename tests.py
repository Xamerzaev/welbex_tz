import os
from flask import Flask
from flask_testing import TestCase
from core.models import *
import unittest
import datetime
from core import app

class MyTest(TestCase):

    def create_app(self):
       
        app.config['TESTING'] = True
        return app

    def test_create_wel(self):
        date = datetime.datetime.now()
        wel = Wel(date=date, title='bus №55', quantity=5, distance=54)
        db.session.add(wel)
        db.session.commit()

        assert wel in db.session

        response = self.client.get("/")

        assert wel in db.session



if __name__ == '__main__':
    unittest.main()