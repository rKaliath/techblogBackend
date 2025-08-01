from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField("/category_image")
    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return self.title
    
class BlogPost(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    images = models.ImageField(upload_to='blog_images/')
    pdf = models.FileField(upload_to='pdf_files/', null=True, blank = True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category, related_name="posts")

    class Meta:
        verbose_name_plural = "blog_posts"

    def __str__(self):
        return self.title 

class BlogImage(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete = models.CASCADE, related_name = 'blog_images')
    image = models.ImageField(upload_to='blog_images/')
    caption = models.CharField(max_length=200, blank=True)

class Comment(models.Model):
    author = models.CharField(max_length=60)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name = 'comments')

    def __str__(self):
        return f"{self.author} on '{self.post}'"
    
