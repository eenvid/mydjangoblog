from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path("", views.articlesList, name ='list'),
    path("<slug>", views.articlesDetails, name = 'details')
]
