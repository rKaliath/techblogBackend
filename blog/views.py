from django.shortcuts import render
from blog.models import BlogPost, Comment, Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer, BlogPostsSerializer


@api_view(['GET'])
def all_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def select_category(request, category_pk):
    category = Category.objects.get(pk = category_pk)
    posts = BlogPost.objects.filter(category = category)
    serializer = BlogPostsSerializer(posts, many = True)
    return Response(serializer.data)


@api_view(['GET'])
def blog_detail(request, post_pk):

    post = BlogPost.objects.get(pk=post_pk)
    serializer = BlogPostsSerializer(post)
    return Response(serializer.data)