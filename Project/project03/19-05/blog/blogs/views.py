from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.


def __check_blogpost_owner(_blogpost, _request):
    if _blogpost.owner != _request.user:
        raise Http404


def index(request):
    """The home page for blogs."""
    # noinspection PyUnresolvedReferences
    my_posts = BlogPost.objects.order_by('date_added')
    context = {'blog_posts': my_posts}
    return render(request, 'blogs/index.html', context)


@login_required
def new_post(request):
    """Add a new blog post."""
    if request.method != 'POST':
        # create a blank form
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            my_new_post = form.save(commit=False)
            my_new_post.owner = request.user
            my_new_post.save()
            return redirect('blogs:index')

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


@login_required
def edit_post(request, post_id):
    """Edit an existing blog post."""
    # noinspection PyUnresolvedReferences
    my_post = BlogPost.objects.get(id=post_id)
    __check_blogpost_owner(my_post, request)
    if request.method != 'POST':
        # pre-fill form with my_post
        my_form = BlogPostForm(instance=my_post)
    else:
        # save edited blog post
        my_form = BlogPostForm(instance=my_post, data=request.POST)
        if my_form.is_valid():
            my_form.save()
            return redirect('blogs:index')

    context = {'post': my_post, 'form': my_form}
    return render(request, 'blogs/edit_post.html', context)
