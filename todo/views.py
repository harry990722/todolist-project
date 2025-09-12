from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from .models import Todo
from .forms import TodoForm


def create_todo(request):
    message = ""
    form = TodoForm()
    # POST
    if request.method == "POST":
        form = TodoForm(request.POST)
        form.save()
        message = "建立成功!"
        return redirect("todolist")

    return render(request, "todo/create-todo.html", {"message": message, "form": form})


def view_todo(request, id):
    todo = None
    try:
        todo = Todo.objects.get(id=id)
    except Exception as e:
        print(e)
    return render(request, "todo/view_todo.html", {"todo": todo})


def todolist(request):
    # order_by 加上 - 號降序
    todos = Todo.objects.all().order_by("-created")

    return render(request, "todo/todolist.html", {"todos": todos})


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello django!</h1>")


def books(request):
    my_books = {1: "python", 2: "Java", 3: "C# book"}

    return HttpResponse(json.dumps(my_books), content_type="application/json")
