from django.shortcuts import render
from django.views.generic import TemplateView


class ForumView(TemplateView):

    template_name = 'forum/index.html'

index = ForumView.as_view()

def index(request):
    return render(request, 'forum/index.html')