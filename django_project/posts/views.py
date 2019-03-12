from django.shortcuts import render
from django.http import HttpResponse

from .models import postsClass

# Create your views here.

def index(request):
    # return HttpResponse('HELLO WORLD')

    posts = postsClass.objects.all()[:10] #number of posts

    context = {
        'title': 'Latest Posts',
        'posts': posts
    }

    return render(request, 'posts/index.html', context)

def details(request, id):
    post = postsClass.objects.get(id = id)

    context = {
            'posts' : post            
        }        

    return render(request, 'posts/details.html', context)
        

