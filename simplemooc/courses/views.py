from django.shortcuts import render

from .models import Course
# Create your views here.

def index(request):
    course = Course.object.all()
    template_name = 'courses/index.html'
    context = {
        'courses': course
    }
    return render(request, template_name, context)

def details(request, pk):
    course = Course.object.get(pk=pk)
    context = {
        'courser': course
    }
    template_name = 'courses/details.html'
    return render(request, template_name, context)