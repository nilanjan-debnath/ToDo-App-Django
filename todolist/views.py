from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, "base.html", {"todo_list":todos})

@require_http_methods(["POST"])
def add(request):
    title = request.POST["title"]
    details = request.POST["details"]
    finishtime = request.POST["finishtime"]
    todo = Todo(title=title, details=details, finishtime=finishtime)
    todo.save()
    return redirect("index")

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    title = request.POST["title"]
    details = request.POST["details"]
    todo.title = title
    todo.details = details
    todo.save()
    return redirect("index")

def complete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.complete = not todo.complete
    todo.save()
    return redirect("index")

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("index")