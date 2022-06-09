from django.views.generic import ListView
from django.shortcuts import render
from .models import Article

# Create your views here.
# def myview (request):
#     return render(request, 'index.html')

# defining a listview to render the content in a list
class ArticleListView(ListView):
    model = Article
    template_name ='index.html'