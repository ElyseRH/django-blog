from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    model = Post  # use Post as its model
    queryset = Post.objects.filter(status=1).order_by('-created_on')  # shows published posts in descending order
    template_name = 'index.html'  # takes index as it's template
    paginate_by = 6  # 6 posts will appear per page
