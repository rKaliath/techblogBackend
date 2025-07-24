from django.urls import path
from .import views

urlpatterns = [
    path("", views.all_categories, name = "categories"),
    path("categories/<int:category_pk>/", views.select_category, name = "blog_posts"),
    path("blog_posts/<int:post_pk>/", views.blog_detail, name = "blog_detail")
]

