from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)
     #This function is used to print title and the author name in the admin page(Post table)
    def __str__(self):
        return self.name
    

    #This function is used to redirect to the article detail post after adding a new post
    def get_absolute_url(self):
       # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')


class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)




class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    header_image = models.ImageField(blank=True,null=True,upload_to="images/")
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    #body = models.TextField()
    body = RichTextField(blank=True,null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255,default='entertainment')
    snippet = models.CharField(max_length=255)


    #This function is used to print title and the author name in the admin page(Post table)
    def __str__(self):
        return self.title + " | " + str(self.author)
    

    #This function is used to redirect to the article detail post after adding a new post
    def get_absolute_url(self):
       # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')