from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path("", views.articlesList, name ='list'),
    path("create", views.create_article, name='create'),
    path("<slug>", views.articlesDetails, name = 'details')
]
