from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=250,db_index=True)

    def __str__(self):
        return self.category

class Juice(models.Model):
    type = models.ForeignKey('Category', on_delete=models.PROTECT,null=True)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='image')
    description = models.TextField()
    price = models.CharField(max_length=250)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/api/juice/{self.id}'



class News(models.Model):
    title = models.CharField("Название", max_length=100)
    image = models.ImageField(upload_to='images')
    details = models.TextField("Подробности")
    price = models.CharField("Цена", max_length=10)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/api/news/{self.id}'


class Register(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.name

#####################

class Shop(models.Model):
    title = models.CharField(max_length=250)
