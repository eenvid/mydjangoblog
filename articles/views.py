from django.shortcuts import render
from . import models

def articlesList(request):
    article = models.articles.objects.all().order_by("date")
    return render(request,"articles/tarticlesList.html", {'articles':article})
