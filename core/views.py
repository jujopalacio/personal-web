from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    """
    The home of our site
    :param request:
    :return:
    """
    content = "<h1> My personal Web </h1><h2>Portada</h2>"
    return HttpResponse(content)