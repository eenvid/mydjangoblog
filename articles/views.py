from django.shortcuts import render, HttpResponse, redirect
from . import models, forms
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
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/createArticle.html', {'form':form})