from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import TodoForm, NewUserForm
from .models import Todo


def index(request):
    item_list = Todo.objects.order_by("-order_id")
    form = TodoForm()
    page = {
        "forms": form,
        "card_list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)


def card_view(request, item_id):
    if item_id == 0:
        form = TodoForm()
        page = {
        "forms": form,
        "title": "TODO LIST",
        }
    else:
        card = Todo.objects.get(id=item_id)
        form = TodoForm(instance=card)
        page = {
            "forms": form,
            "card": card,
            "title": "TODO LIST",
        }
    return render(request, "todo/card_view.html", page)


def save(request, item_id):
    card = Todo.objects.get(id=item_id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
    messages.info(request, "Item saved!")
    return redirect('todo')


def new(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Item saved!")
        else:
            messages.error(request, "Error!")
    return redirect('todo')


def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Item removed!")
    return redirect('todo')


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="todo/register.html", context={"register_form":form})