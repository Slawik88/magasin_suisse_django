from django.shortcuts import render, get_object_or_404

from .models import Category, Swiper, Product


# Create your views here.

def index_page_view(request):
    categories = Category.objects.all()
    swiper_images = Swiper.objects.all()

    context = {
        'categories': categories,
        'swiper_images': swiper_images,

    }


    return render(request, 'catalogApp/index.html', context=context)

def get_categoris_and_subcategories_and_product(request, category_slug):
    try:
        
        category = get_object_or_404(Category, category_slug=category_slug)
        subcategories = category.get_children()

        products = Product.objects.filter(product_category_id=category)
        swiper_images = Swiper.objects.all()

        context = {'category': category, 
                   'subcategories': subcategories, 
                   'products': products,
                   'swiper_images': swiper_images,

        }
        
        return render(request, 'catalogApp/subcategories_and_products.html', context=context)
    except Category.DoesNotExist:
        return render(request, 'catalogApp/not_found_subcategories.html', {'error': 'Category not found'}, status=404)

def product_details_page(request, product_slug):
        
    products = Product.objects.filter(product_slug=product_slug)

    context = {
        'products': products,
    }

    return render(request, 'catalogApp/product_detail.html', context=context)