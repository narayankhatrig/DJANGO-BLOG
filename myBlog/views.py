from django.shortcuts import render

from myBlog.models import Post

# Create your views here.

def view_post(request):
    posts = Post.objects.all()
    return render(
        request,
        "view_post.html",
        {"posts": posts},
    )
