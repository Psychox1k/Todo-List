from django.shortcuts import render
from django.views import generic

from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/index.html"

class TagListView(generic.ListView):
    model = Tag

