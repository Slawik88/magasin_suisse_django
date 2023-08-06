from django.shortcuts import render

from .models import Category


# Create your views here.

def index_page_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }


    return render(request, 'catalogApp/index.html', context=context)

def get_subcategories(request, category_slug):
    try:
        category = Category.objects.get(category_slug=category_slug)
        subcategories = category.get_children()
        return render(request, 'catalogApp/subcategories.html', {'subcategories': subcategories})
    except Category.DoesNotExist:
        return render(request, 'catalogApp/subcategories.html', {'error': 'Category not found'}, status=404)