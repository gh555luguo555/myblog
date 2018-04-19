from django.shortcuts import render
from django.views import View
from .models import Article
from django.http import HttpResponse

# Create your views here.
class Index(View):
    def get(self, request):
        articles = Article.objects.all()
        print(articles[0].img)
        return render(request, 'index.html', {'articles':articles})


