from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def newsView(request):
    return HttpResponse("Hello Web from view function. Ate, Olger QV")