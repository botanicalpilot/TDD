from django.shortcuts import render
'''
Render takes the request as its first parameter and the name of the template to render. Django automatically looks for folders called 'templates' inside the apps dir and build an HttpResponse automatically so the programmer doesn't have to. 
'''

def home_page(request):
    return render (request, 'home.html')