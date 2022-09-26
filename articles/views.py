from django.shortcuts import render, HttpResponse
from . import models

def articlesList(request):
    article = models.articles.objects.all().order_by("-date")
    return render(request,"articles/tarticlesList.html", {'articles':article})


def articlesDetails(request, slug):
    article =  models.articles.objects.get(slug = slug)
    return render(request, 'articles/articleDetails.html', {'article':article})