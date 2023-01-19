from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """main page for the learning_logs app"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """render all of the topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)