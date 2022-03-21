from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Author(models.Model):
    name = models.CharField(verbose_name='name', max_length=30)
    surname = models.CharField(verbose_name='surname', max_length=30)


class Category(models.Model):
    name = models.CharField(verbose_name='name', max_length=30)


class Tag(models.Model):
    name = models.CharField(verbose_name='name', max_length=30)


class Article(models.Model):
    name = models.CharField( max_length=30)
    argument = models.CharField(max_length=50)
    content = models.TextField()
    auth_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags_id = models.ManyToManyField(Tag)
    date_of_pub = models.DateField(verbose_name='date_of_publication')

