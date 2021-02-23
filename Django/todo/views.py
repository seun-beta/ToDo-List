from django.http import HttpResponse, response
from django.http import HttpResponseRedirect
from django.utils import html
from django.views import View
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(request, 'todo/home.html')