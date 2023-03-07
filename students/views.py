from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from students.models import Student


def students(request):
    mystudents = Student.objects.all().values()
    template = loader.get_template('all_students.html')
    context = {
        'mystudents': mystudents,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'all_students.html', context=context)


def home_page(request):
    # default to Stranger if no user_name provided
    name = request.GET.get("user_name", "Stranger")
    message = f"<html><h1>Welcome {name} to my Website</h1></html>"
   # return HttpResponse(message)
    # return render(request, 'base.html')
    return render(request, 'base.html', {'name': name})
