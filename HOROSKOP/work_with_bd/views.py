from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Person


# получение данных из бд
def index(request):
    people = Person.objects.all()
    return render(request, "includes/index.html", {"people": people})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        person = Person()
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
    return HttpResponseRedirect("/work_with_bd/")


# изменение данных в бд
def edit(request, id):
    try:
        person = Person.objects.get(id=id)

        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/work_with_bd/")
        else:
            return render(request, "includes/edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/work_with_bd/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")