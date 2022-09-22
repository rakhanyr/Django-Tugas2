from django.test import TestCase, Client
from django.urls import reverse
from mywatchlist.models import WatchList

# Create your tests here.
class UnitTesting(TestCase):
    def test_app_url_exists(self):
        response = Client().get('http://localhost:8000/mywatchlist/html/')
        self.assertEqual(response.status_code,200)
class AppTest(TestCase):
    def test_app_url_exists(self):
        response = Client().get('http://localhost:8000/mywatchlist/json/')
        self.assertEqual(response.status_code,200)

class AppTest(TestCase):
    def test_app_url_exists(self):
        response = Client().get('http://localhost:8000/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)

