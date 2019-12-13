from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        #resolve is a Django function to resolve URLS and find what view f(x) they should map to. 
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        #create a HttpRequest object which will be seen by Django when a user's browsers asks for homepage. 
        request = HttpRequest()
        #pass the request to the home_page, which gives response
        response = home_page(request)
        #extract the .content of the response in the form of raw bytes which must be decoded to UTF8
        html = response.content.decode('utf8')
        #make sure it starts with html tag
        self.assertTrue(html.startswith('<html>'))
        #we want a tag with To-Do lists in it somewhere in the html file. 
        self.assertIn('<title>To-Do lists</title>', html)
        #make sure it ends with html tag
        self.assertTrue(html.endswith('</html>'))