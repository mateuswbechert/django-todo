from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from .forms import TodoForm
from .models import Todo


def index(request):
    item_list = Todo.objects.order_by("-order_id")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    page = {
        "forms": form,
        "card_list": item_list,
        "title": "TODO LIST",
    }

    return render(request, 'todo/index.html', page)


def card_view(request, item_id):
    card = Todo.objects.get(id=item_id)
    form = TodoForm()
    page = {
        "forms": form,
        "card": card,
        "title": "TODO LIST",
    }
    return render(request, "todo/card_view.html", page)


def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Item removed!")
    return redirect('todo')
