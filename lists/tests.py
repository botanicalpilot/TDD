'''
Unit tests are about testing logic, flow control, and configuration. Don't. Test. Constants.
'''


from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page


class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/') 
        self.assertTemplateUsed(response, 'home.html')

    # def test_home_page_returns_correct_html(self):
    #     #instead of manually creating an HttpResponse object can then calling view, 
    #     # we can call self.client.get and pass the URL we want to test.
    #     response = self.client.get('/')

    #     html = response.content.decode('utf8')
    #     self.assertTrue(html.startswith('<html>'))
    #     self.assertIn('<title>To-Do lists</title>', html)
    #     self.assertTrue(html.strip().endswith('</html>'))

    #     #.assertTemplateUsed is the test method that Django TestCase class provides. 
    #     # This method checks what template was used to render a response, 
    #     # but will only work for responses that were retrieved by the test client. 
    #     self.assertTemplateUsed(response, 'home.html')