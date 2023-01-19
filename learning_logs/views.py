from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm

# Create your views here.


def index(request):
    """main page for the learning_logs app"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """render all of the topics"""
    topics = Topic.objects.order_by('date_added')
    count = len(topics)
    context = {'topics': topics, 'count':count}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """render the details about a specific topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    count = len(entries)
    context = {'topic': topic, 'entries': entries, 'count': count}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """add new topic"""
    if request.method != 'POST':
        # the user did not provide any data
        form = TopicForm()
    else:
        # the user did provide some data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Dodanie nowego wpisu dla określonego tematu."""
    topic = Topic.objects.get(id=topic_id) 
    if request.method != 'POST': 
        # Nie przekazano żadnych danych, należy utworzyć pusty formularz.
        form = EntryForm() 
    else:
        # Przekazano dane za pomocą żądania POST, należy je przetworzyć.
        form = EntryForm(data=request.POST) 

    if form.is_valid():
        new_entry = form.save(commit=False) 
        new_entry.topic = topic 
        new_entry.save()
        return redirect('learning_logs:topic', topic_id=topic_id) 
    # Wyświetlenie pustego formularza.

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)