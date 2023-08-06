from django.shortcuts import render

from .models import Category


# Create your views here.

def index_page_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }


    return render(request, 'mainapp/index.html', context=context)
