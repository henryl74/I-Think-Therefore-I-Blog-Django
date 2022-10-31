from django.shortcuts import render
from django.views import generic
# from django.http import HttpResponseRedirect
# from django.contrib import messages
from .models import Post
# from .forms import CommentForm

# Create your views here.


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
