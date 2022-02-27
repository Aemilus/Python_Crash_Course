from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.


def __check_topic_owner(_topic, _request):
    # verify topic belongs to current user
    if _topic.owner != _request.user:
        raise Http404


def index(request):
    """The home page for Learning Logs."""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """Show all topics."""
    # noinspection PyUnresolvedReferences
    my_topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': my_topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """Show a single topic identified by id and all its entries."""
    # noinspection PyUnresolvedReferences
    my_topic = Topic.objects.get(id=topic_id)
    __check_topic_owner(my_topic, request)
    # the minus sign in front of date_added sorts the results in reverse order,
    # which will display the most recent entries first
    entries = my_topic.entry_set.order_by('-date_added')
    context = {'topic': my_topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # no data submitted; create a blank form
        my_form = TopicForm()
    else:
        # POST data submitted; process the data
        my_form = TopicForm(data=request.POST)
        if my_form.is_valid():
            my_new_topic = my_form.save(commit=False)
            my_new_topic.owner = request.user
            my_new_topic.save()
            return redirect('learning_logs:topics')
    # display a blank or invalid form
    context = {'form': my_form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry on a specific topic."""
    # noinspection PyUnresolvedReferences
    my_topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # no data submitted; create a blank form
        my_form = EntryForm()
    else:
        # POST data submitted; process the data
        my_form = EntryForm(data=request.POST)
        if my_form.is_valid():
            my_new_entry = my_form.save(commit=False)
            my_new_entry.topic = my_topic
            my_new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    # display a blank or invalid form
    context = {'topic': my_topic, 'form': my_form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    # noinspection PyUnresolvedReferences
    my_entry = Entry.objects.get(id=entry_id)
    my_topic = my_entry.topic
    __check_topic_owner(my_topic, request)

    if request.method != 'POST':
        # initial request; pre-fill form with current entry in database
        my_form = EntryForm(instance=my_entry)
    else:
        # POST data submitted; process data
        my_form = EntryForm(instance=my_entry, data=request.POST)
        if my_form.is_valid():
            my_form.save()
            return redirect('learning_logs:topic', topic_id=my_topic.id)

    context = {'entry': my_entry, 'topic': my_topic, 'form': my_form}
    return render(request, 'learning_logs/edit_entry.html', context)
