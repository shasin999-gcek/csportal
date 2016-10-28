from django.shortcuts import render
from django.http import HttpResponse
from .models import Students

# Create your views here.
def test(request) :
    return HttpResponse("<h1> welcome to cs portal </h1>")
def student(request) :
    students = Students.objects.all()
    return render(request,"index.html",{'students': students})
