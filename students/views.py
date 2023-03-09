from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from students.models import Student


def all_students(request):
    all_students = Student.objects.all()
    return render(request, 'all_students.html', {'all_students': all_students})


def students_detail(request, id):
    students_detail = Student.objects.get(id=id)

    return render(request, 'detail.html', {'detail': students_detail})


def home_page(request):
    # default to Stranger if no user_name provided
    name = request.GET.get("user_name", "Stranger")
    message = f"<html><h1>Welcome{name} to my Website</h1></html>"
   # return HttpResponse(message)
    # return render(request, 'base.html')
    return render(request, 'base.html', {'name': name})
