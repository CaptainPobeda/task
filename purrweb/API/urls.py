from django.contrib import admin
from django.urls import path
from API.views import *

app_name = 'API'
urlpatterns = [
    path('article/<int:pk>/', ArticleListView_2.as_view()),
    path('author', AuthorListView.as_view()),
    path('category', CategoryListView.as_view()),
    path('tag', TagListView.as_view()),
    path('date', DateListView.as_view()),
]