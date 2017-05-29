from django.shortcuts import render, get_object_or_404

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
    course = get_object_or_404(Course, pk=pk)
    context = {
        'course': course
    }
    template_name = 'courses/details.html'
    return render(request, template_name, context)