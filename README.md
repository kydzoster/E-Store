1. **pip3 install django**
2. **django-admin startproject botique_ado .**
3. **python3 manage.py runserver**
4. **python3 manage.py migrate**
5. **python3 manage.py createsuperuser**

        username: kydzoster
        password: pass123

6. **pip3 install django-allauth**
7. *Copy **AUTHENTICATION_BACKENDS** from **https://django-allauth.readthedocs.io/en/latest/installation.html** and paste them under **TEMPLATES** in **settings.py***

        AUTHENTICATION_BACKENDS = [
            # Needed to login by username in Django admin, regardless of `allauth`
            'django.contrib.auth.backends.ModelBackend',

            # `allauth` specific authentication methods, such as login by e-mail
            'allauth.account.auth_backends.AuthenticationBackend',
        ]

    *and copy few **INSTALLED_APPS** from the same website and paste inside **INSTALLED_APPS** in **settings.py***

        'django.contrib.sites',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',

8. Inside settings.py under AUTHENTICATION_BACKENDS add:

        SITE_ID = 1

9. inside urls.py create a new path inside urlpatterns:

        path('accounts/', include('allauth.urls'))

    and import **include** from **django.urls**

10. **python3 manage.py migrate**
11. *run server - **python3 manage.py runserver**, then in address bar at the end type **/admin**, when promted log-in, click on **sites**, click on **example.com**, change Domain Name to **botiqueado.example.com** and change Display name to E-Store*
12. In settings.py under SITE_ID add:

        EMAIL_BACKEND = 'django.core.email.backends.console.EmailBackend'

        ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
        ACCOUNT_EMAIL_REQUIRED = True
        ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
        ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
        ACCOUNT_USERNAME_MIN_LENGTH = 4
        LOGIN_URL = '/accounts/login/'
        LOGIN_REDIRECT_URL = '/'

13. **pip3 freeze > requirements.txt**
14. **mkdir templates**
15. **mkdir templates/allauth**
16. **cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth/** *this will copy every single allauth template so we can customize them.*
17. delete **openid** and **tests** from *templates/allauth* folder
18. **touch templates/base.html**
19. use Boostrap *Starter Template* from - **https://getbootstrap.com/docs/4.5/getting-started/introduction/**
20. change newly added templates/base.html to: 

        <!doctype html>
        {% load static %}

        <html lang="en">
        <head>

            {% block meta %}
                <meta http-equiv="X-UA-Compatible" content="ie=edge">
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            {% endblock %}

            {% block extra_meta %}
            {% endblock %}

            {% block corecss %}
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
            {% endblock %}

            {% block extra_css %}
            {% endblock %}

            {% block corejs %}
                <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
                <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
            {% endblock %}

            {% block extra_js %}
            {% endblock %}

            <title>E-Store {% block extra_title %}{% endblock %}</title>
        </head>
        <body>
            <header class="container-fluid fixed-top"></header>

            {% if messages %}
                <div class="message-container"></div>
            {% endif %}

            {% block page_header %}
            {% endblock %}

            {% block content %}
            {% endblock %}

            {% block postloadjs %}
            {% endblock %}

        </body>
        </html>

21. **python3 manage.py startapp home**
22. **mkdir -p home/templates/home**
23. **touch home/templates/home/index.html** *-then add in index.html:*

        <!doctype html>
        {% extends "base.html" %}
        {% load static %}

        {% block content %}
            <h1 class="display-4 text-success">It works!</h1>
        {% endblock %}

24. in home/views.py add:

        def index(request):
            """ A view to return the index page """
            return render(request, 'home/index.html')

25. touch home/urls.py and add:

        from django.contrib import admin
        from django.urls import path
        from .import views

        urlpatterns = [
            path('', views.index, name='home')
        ]

26. go to botique_ado/urls.py and add a path to urlpatterns:

        path('', include('home.urls')),

27. go to botique_ado/settings.py and add to INSTALLED_APPS:

        'home',

    then in TEMPLATES inside DIRS add:

        os.path.join(BASE_DIR, 'templates'),
        os.path.join(BASE_DIR, 'templates', 'allauth'),

28. Add content in **index.html** and **base.html**
29. **mkdir static** is for css, js and other static files, then **mkdir static/css** and then **mkdir media** which will hold images.
30. **touch static/css/base.css**
31. under STATIC_URL add:

        STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

32. for jango to see these urls, go to botique_ado/urls.py and import:

        from django.conf import settings
        from django.conf.urls.static import static

    and add at the end of the urlpatterns:

        urlpatterns = [
            ...
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

33. **mkdir templates/includes**
34. **touch templates/includes/main-nav.html** then copy content from *https://github.com/ckz8780/boutique_ado_v1/blob/e77fa8e928e3901d3502b18e912e90d2204b8ec3/templates/includes/main-nav.html*
35. **touch templates/includes/mobile-top-header.html** then copy content from *https://github.com/ckz8780/boutique_ado_v1/blob/e77fa8e928e3901d3502b18e912e90d2204b8ec3/templates/includes/mobile-top-header.html*
36. **python3 manage.py startapp products**
37. *add this app to botique_ado/settings.py inside INSTALLED_APPS:*

        products

38. **mkdir products/fixtures** *- fixtures are used to load data into django DB so we do not have to do it manually in the admin*
39. *use **jsonformatter.org** to neatly organise JSON output in fixtures folder.*
40. products/models.py add a new classes:

        class Category(models.Model):
            name = models.CharField(max_length=254)
            # null in DB and blank in form
            friendly_name = models.CharField(max_length=254, null=True, blank=True)

            def __str__(self):
                return self.name

            def get_friendly_name(self):
                return self.friendly_name

        class Product(models.Model):
            category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
            sku = models.CharField(max_length=254, null=True, blank=True)
            name = models.CharField(max_length=254)
            description = models.TextField()
            price = models.DecimalField(max_digits=6, decimal_places=2)
            rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
            image_url = models.URLField(max_length=1024, null=True, blank=True)
            image = models.ImageField(null=True, blank=True)

            def __str__(self):
                return self.name

41. check **test run** aka **dry run** to make sure if everything is okay. **python3 manage.py makemigrations --dry-run**
42. it returned error for image field, so we will install pillow. **pip3 install pillow** then dry-run again.
43. it cam back with no errors, we can run real migrations. **python3 manage.py makemigrations**
44. **python3 manage.py migrate** - to migrate all apps, however, it is better to migrate specific app to avoid unintentionall migrations of unwanted apps.
45. products/admin.py and add:

        from .models import Product, Category

        admin.site.register(Product)
        admin.site.register(Category)

46. **python3 manage.py loaddata categories** then **python3 manage.py loaddata products** to use fixtures
47. runserver and then in address bar add: **/admin/products/product** to view them.
48. products/models.py add a meta class inside Category(..):

        # this will fix spelling issue and make it plural
        class Meta:
            verbose_name_plural = 'Categories'

49. products/admin.py create 2 classes:

        class ProductAdmin(admin.ModelAdmin):
            list_display = (
                'sku',
                'name',
                'category',
                'price',
                'rating',
                'image',
            )

            ordering = ('sku',)

        class CategoryAdmin(admin.ModelAdmin):
            list_display = (
                'friendly_name',
                'name',
            )

        admin.site.register(Product, ProductAdmin)
        admin.site.register(Category, CategoryAdmin)

50. products/views.py:

        from django.shortcuts import render
        from .models import Product

        def all_products(request):
            """ This will show all products, searches and sorting """
            products = Product.objects.all()

            context = {
                'products': products,
            }

            return render(request, 'products/products.html', context)

51. **touch products/urls.py** then add:

        from django.urls import path
        from . import views

        urlpatterns = [
            path('', views.all_products, name='products')
        ]

52. botique_ado/urls.py add newly created path:

        path('products/', include('products.urls')),

53. **mkdir -p products/templates/products**
54. **touch products/templates/products/products.html** and add:

        {% extends "base.html" %}
        {% load static %}

        {% block page_header %}
            <div class="container header-container">
                <div class="row">
                    <div class="col"></div>
                </div>
            </div>
        {% endblock %}

        {% block content %}
            <div class="container">
                <div class="row">
                    <div class="col">
                        {{ products }}
                    </div>
                </div>
            </div>
        {% endblock %}

55. products/views.py add an import to django.shortcuts:

        get_object_or_404

    and define product_detail:

        def product_detail(request, product_id):
        """ A view to show individual product details """
        product = get_object_or_404(Product, pk=product_id)

        context = {
            'product': product,
        }

        return render(request, 'products/product_detail.html', context)

56. products/urls.py add new path:

        path('<product_id>', views.product_detail, name='product_detail'),

57. duplicate **products.html** and rename it to **product_detail.html**
58. products/views.py replace all_products:

        def all_products(request):
            """ This will show all products, searches and sorting """
            products = Product.objects.all()
            query = None

            if request.GET:
                if 'q' in request.GET:
                    query = request.GET['q']
                    if not query:
                        messages.error(request, "You did not enter any search criteria!")
                        return redirect(reverse('products'))

                    queries = Q(name__icontains=query) | Q(description__icontains=query)
                    products = products.filter(queries)

            context = {
                'products': products,
                'search_term': query,
            }

            return render(request, 'products/products.html', context)

59. for javascript to work on products.html with not only sorting by numbers but also by names in the products/views.py need to import:

        from django.db.models.functions import Lower

60. **python3 manage.py startapp bag** and add it to botique_ado/settings.py
61. ...