from django.http import HttpResponse, response
from django.http import HttpResponseRedirect
from django.utils import html
from django.views import View
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Task

# Create your views here.

def index(request):
    data = Task.objects.values()
    print(len(data))
    for i in data:
        print(i)
        id = i['id']
        task = i['task']
        task_description = i['task_description']
    context = {'data' : data}
    return render(request, 'todo/home.html', context)

class Edit(View):
    def get(request, id):


        return render(request, 'todo/edit.html')

    def get(request):
        pass

class New(View):
    def get(self, request):
        return render(request, 'todo/new.html')

    def post(self, request):
        response_task = request.POST.get('task')
        response_task_description = request.POST.get('task_description')
        t = Task(task=response_task, task_description=response_task_description)
        t.save()
        return HttpResponseRedirect('success')


class Success(View):
    def get(self, request):
        return render(request, 'todo/success.html')


