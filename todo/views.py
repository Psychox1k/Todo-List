from django.shortcuts import render
from django.views import generic

from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/index.html"
    paginate_by = 10

class TagListView(generic.ListView):
    model = Tag
    paginate_by = 10

