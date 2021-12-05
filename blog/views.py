from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    model = Post  # use Post as its model
    queryset = Post.objects.filter(status=1).order_by('-created_on')  # shows published posts in descending order
    template_name = 'index.html'  # takes index as it's template
    paginate_by = 6  # 6 posts will appear per page


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)  # only search published posts
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        #below checks if user has liked comments and shows
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )