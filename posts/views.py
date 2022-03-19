from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
# Create your views here.
def index(request):
    #If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
    #If the form is valid
        if form.is_valid():
            form.save()
    #Yes Save
    #Redirect to home
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    #no, show error

    #Get all posts
    posts = Post.objects.all().order_by('-created_at')[:20]


    return render(request, 'posts.html',
                {'posts': posts})

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def like(request, post_id):
    newlikecount = Post.objects.get(id=post_id)
    newlikecount.likecount += 1
    newlikecount.save()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    posts = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=posts)
    #If the form is valid
        if form.is_valid():
            form.save()
    #Yes Save
    #Redirect to home
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    return render(request, 'edit.html',
                {'posts': posts})