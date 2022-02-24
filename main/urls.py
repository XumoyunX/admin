from django.urls import path
from .views import *

# app_name = "main"

urlpatterns = [
    path("", index, name="index"),
    path("blog_details/", blog_details, name="blog_details"),
    path("blog/", blog, name="blog")
]