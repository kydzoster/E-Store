from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category

# Create your views here.


def all_products(request):
    """ This will show all products, search and sort"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        # check if sort is in request.get
        if 'sort' in request.GET:
            # if it is, we set it equal to both sort, which is none
            sortkey = request.GET['sort']
            # rename sort to sortkey to use it as a fieldname
            sort = sortkey
            if sortkey == 'name':
                # we rename sortkey to fit the field name if the user is sorting by name
                sortkey = 'lower_name'
                # we annotate current list of products with a new field
                products = products.annotate(lower_name=Lower('name'))

            if sortkey == 'category':
                sortkey = 'category__name'

            # we check if there is a direction
            if 'direction' in request.GET:
                direction = request.GET['direction']
                #we check if it is descending and decide wether to reverse the order
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            # sort the products
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
    # returns current sorting methodology to the template
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
