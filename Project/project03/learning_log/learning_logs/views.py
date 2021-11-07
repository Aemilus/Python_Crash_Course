from django.shortcuts import render

# Create your views here.
from .models import Topic


def index(request):
    """The home page for Learning Logs."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Show a single topic identified by id and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    # the minus sign in front of date_added sorts the results in reverse order,
    # which will display the most recent entries first
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
