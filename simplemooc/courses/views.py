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