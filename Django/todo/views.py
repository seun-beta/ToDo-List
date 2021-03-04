from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.urls import reverse


from .models import Task

class TaskList(ListView):
    model = Task
    context_object_name = 'my_tasks'
    template_name = 'todo/task_list.html'
    
class Edit(View):
    def get(self, request, number):
        task = Task.objects.get(pk=number)
        context = {'task' : task }

        return render(request, 'todo/edit.html', context)

    def post(self, request, number):
        if request.POST.get('submit_task'):
            edit_task = request.POST.get('edit_task')
            edited_task = Task.objects.filter(pk=number).update(task=edit_task)

        elif request.POST.get('delete_task'):
            delete_task = request.POST.get('edit_task')
            delete_task = Task.objects.filter(pk=number).delete()



        return render(request, 'todo/edit_success.html')
        

class New(View):
    def get(self, request):
        return render(request, 'todo/new.html')

    def post(self, request):
        response_task = request.POST.get('task')
        task = Task(task=response_task)
        task.save()
        return render(request, 'todo/new_success.html')


class Success(View):
    def get(self, request):
        return render(request, 'todo/success.html')
