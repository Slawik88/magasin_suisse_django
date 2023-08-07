from django.shortcuts import render, get_object_or_404

from .models import Category, Swiper


# Create your views here.

def index_page_view(request):
    categories = Category.objects.all()
    swiper_images = Swiper.objects.all()

    context = {
        'categories': categories,
        'swiper_images': swiper_images,

    }


    return render(request, 'catalogApp/index.html', context=context)

def get_categoris_and_subcategories(request, category_slug):
    try:
        category = get_object_or_404(Category, category_slug=category_slug)
        subcategories = category.get_children()
        return render(request, 'catalogApp/subcategories.html', {'category': category, 'subcategories': subcategories})
    except Category.DoesNotExist:
        return render(request, 'catalogApp/not_found_subcategories.html', {'error': 'Category not found'}, status=404)