from django.urls import path
from myBlog import views

urlpatterns = [
    path("", views.view_post, name="view_post"),
]

