from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.

class NewsPageView(ListView):
    template_name = "news.html"
