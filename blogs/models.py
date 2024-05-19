from django.db import models
from users.models import *

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE , related_name='posts')
    published_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='./static/blog_posts', blank=True, null=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    def __str__(self):
        return self.title

class Comment(models.Model):
    id=models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True,related_name='comments')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        if self.author:
            return f'Comment {self.id} by {self.author.first_name} on {self.post.title}'
        else:
            return f'Comment {self.id} on {self.post.title}'
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "categories"  
    def __str__(self):
        return self.name
