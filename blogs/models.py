from django.contrib.auth import get_user_model
from django.db import models
from common.models import BaseModel

UserModel = get_user_model()

class BlogCategoryModel(BaseModel):
    title = models.CharField(max_length=128)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'



class BlogTagModel(models.Model):
    title = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Blog Tag'
        verbose_name_plural = 'Blog Tags'

class BlogModel(models.Model):
    title = models.CharField(max_length=128)
    image1 = models.ImageField(upload_to='blogs')
    image2 = models.ImageField(upload_to='blogs')
    short_description = models.CharField(max_length=255, blank=True, null=True)
    long_description = models.TextField(max_length=1024, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    categories = models.ManyToManyField(BlogCategoryModel, related_name='blogs')
    tags = models.ManyToManyField(BlogTagModel, related_name='blogs')


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

class BlogCommentModel(models.Model):
    comment = models.CharField(max_length=128)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='blog_comments')
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Blog Comment'
        verbose_name_plural = 'Blog Comments'

class BlogLikeModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='blog_likes')
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='likes')
    

    def __str__(self):
        return f'{self.user.get_full_name()} liked to {self.blog.title}'
    
    class Meta:
        verbose_name = 'Blog Like'
        verbose_name_plural = 'Blog Likes'



        