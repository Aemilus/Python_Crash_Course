from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.


def index(request):
    """The home page for blogs."""
    blog_posts = BlogPost.objects.order_by('date_added')
    context = {'blog_posts': blog_posts}
    return render(request, 'blogs/index.html', context)


def new_post(request):
    """Add a new blog post."""
    if request.method != 'POST':
        # create a blank form
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


# def edit_post(request, post_id):
#     """Edit an existing blog post."""
#     blog_post = BlogPost.objects.get(id=post_id)
