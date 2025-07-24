from django.contrib import admin
from blog.models import Category, Comment, BlogPost

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogPost, PostAdmin)
admin.site.register(Comment, CommentAdmin)


