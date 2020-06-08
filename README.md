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
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
            
            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
        
            <title>E-Store</title>
        </head>
        <body>

        </body>
        </html>