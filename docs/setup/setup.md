### SETUP :

- `brew install python`
- `python3.11 --version` : check version installed
- `python3.11 -m venv .venv`
- `.venv/bin/activate`
- access was denied. Ran `chmod +x .venv/bin/activate` before running above line again
- `source .venv/bin/activate`
- `. .venv/bin/activate`

### Django :

- Start a Django project : `django-admin startproject projectName .`
- Start a Django app : `python3 manage.py startapp AppNameHere`
- each django app needs to be added to the `INSTALLED_APPS` in `settings.py`:

```
'contact',
'locations',
'hours',
'practitioners',
'services',
```

### PACKAGES :

```
pip3 install 'django<4'
pip install django-cloudinary-storage==0.3.0
python -m pip install Pillow
pip3 install djangorestframework
pip install django-filter
pip3 install dj-rest-auth==2.1.9
pip install 'dj-rest-auth[with_social]'
pip install djangorestframework-simplejwt
```

- remember to run `pip3 freeze --local > requirements.txt` at the end of installation
- the following packages also need to be added to `INSTALLED_APPS`:

```
'cloudinary',
'rest_framework',
'django_filters',
'rest_framework.authtoken',
'dj_rest_auth',
'django.contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount',
'dj_rest_auth.registration',
```

- Add additional variables to `sesttings.py`:

```
SITE_ID = 1

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )]
}

REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
```

- url paths need to be added to the project `urls.py` file as well:

```
path('api-auth/', include('rest_framework.urls')),
path('dj-rest-auth/', include('dj_rest_auth.urls')),
path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
```

### ENV.PY :

```
import os
os.environ['CLOUDINARY_URL'] = 'cloudinary://yourAPIEnvironmentVariable'
os.environ['DEV'] = '1'
```
