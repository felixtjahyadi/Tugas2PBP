from multiprocessing.connection import Client
from urllib import response
from django.test import TestCase, Client
from django.urls import resolve
# Create your tests here.

class MyWatchListTest (TestCase):
    def test_mywatchlist_html_exits(self):
        response = Client().get('/mywatchlist/html')
        self.assertEqual(response.status_code,200)

    def test_mywatchlist_xml_exits(self):
        response = Client().get('/mywatchlist/xml')
        self.assertEqual(response.status_code,200)

    def test_mywatchlist_json_exits(self):
        response = Client().get('/mywatchlist/json')
        self.assertEqual(response.status_code,200)