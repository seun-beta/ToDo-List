from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from todo.models import Task

class HomeView(View):
    def get(self, request):
        task = Task.objects.all()
        ctx = { 'task_list' : task }
        return render(request, 'todo/home.html', ctx)


class TaskNew(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todo:home')
    


class TaskEdit(UpdateView):
    model = Task
    success_url = reverse_lazy('todo:home')
    fields = ['task', 'description']


class TaskDelete(DeleteView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todo:home')

