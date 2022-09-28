from django.shortcuts import render, HttpResponse
from . import models
from django.contrib.auth.decorators import login_required
import time


def articlesList(request):
    article = models.articles.objects.all().order_by("-date")
    return render(request,"articles/tarticlesList.html", {'articles':article})


def articlesDetails(request, slug):
    article =  models.articles.objects.get(slug = slug)
    return render(request, 'articles/articleDetails.html', {'article':article})

@login_required(login_url= "/accounts/login")
def create_article(request):
    return render(request, 'articles/createArticle.html')