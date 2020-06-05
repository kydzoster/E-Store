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

        path('accounts', include('allauth.urls'))

    and import **include** from **django.urls**

10. **python3 manage.py migrate**
11. *run server - **python3 manage.py runserver**, then in address bar at the end type **/admin**, when promted log-in, click on **sites**, click on **example.com**, change Domain Name to **botiqueado.example.com** and change Display name to E-Store*
