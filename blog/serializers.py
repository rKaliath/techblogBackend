from .models import BlogPost, Comment, Category

from rest_framework import serializers

class BlogPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = "__all__"
