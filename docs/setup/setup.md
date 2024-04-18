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
- migrate changes after each app:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

### PACKAGES :

`pip3 install` the following packages :

- `'django<4'`
- `django-cloudinary-storage==0.3.0`
- `python -m pip install Pillow`
- `djangorestframework`
- `django-filter`
- `dj-rest-auth==2.1.9`
- `'dj-rest-auth[with_social]'`
- `djangorestframework-simplejwt`
- `psycopg2-binary` _required for psycopg2_
- `dj_database_url==0.5.0 psycopg2`
- `gunicorn`
- `django-cors-headers`
- `whitenoise` _format django admin panel in prod_


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
'corsheaders',
```

- Add an import statement `import dj_database_url`
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
JWT_AUTH_SAMESITE = 'None'
```

- update DB settings : hosting now done by [NEON](https://console.neon.tech/app/projects)

```
if 'DEV' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('PGDATABASE'),
            'USER': os.environ.get('PGUSER'),
            'PASSWORD': os.environ.get('PASSWORD'),
            'HOST': os.environ.get('PGHOST'),
            'PORT': os.environ.get('PGPORT', 5432),
            'OPTIONS': {
                'sslmode': 'require',
            },
        }
    }
```

- update `ALLOWED_HOSTS = ['localhost', 'shs-drf.herokuapp.com']`

- add line to top of `MIDDLEWARE` array :
```
'corsheaders.middleware.CorsMiddleware',
```
- still inside `MIDDLEWARE` directly beneath `SecurityMiddleware`, add:
```
'whitenoise.middleware.WhiteNoiseMiddleware',
```

- below `MIDDLEWARE` add `ALLOWED_ORIGINS`

```
if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]
else:
    CORS_ALLOWED_ORIGIN_REGEXES = [
        r"^https://.*\.gitpod\.io$",
    ]

CORS_ALLOW_CREDENTIALS = True
```

- finally for whitenoise, add the following STATIC settings:
```
if 'DEV' in os.environ:
    STATICFILES_DIRS = os.path.join(BASE_DIR, 'static')
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

### SETTINGS.PY :

- update the following variables:

```
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = 'DEV' in os.environ
```

### URLS.PY :

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
os.environ['SECRET_KEY'] = "nice try"
os.environ['PGHOST']='ep-old-firefly-a2zzo1bv.eu-central-1.aws.neon.tech'
os.environ['PGDATABASE']='****'
os.environ['PGUSER']='****'
os.environ['PGPASSWORD']='*****'
```

### PROCFILE :

- create a `Procfile`
- in it, save:

```
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn projectName.wsgi
```

### HEROKU :

- add the following key/value pairs to `configvars`
- key: `DATABASE_URL` | value: `same as env.py file`
- key: `SECRET_KEY` | value: `same as env.py file`
- key: `CLOUDINARY_URL` | value: `same as env.py file`
- key: `PGHOST` | value: `same as env.py file`
- key: `PGDATABASE` | value: `same as env.py file`
- key: `PGUSER` | value: `same as env.py file`
- key: `PGPASSWORD` | value: `same as env.py file`
- key: `DISABLE_COLLECTSTATIC` | value: `1`

### DJANGO EMAILS :
- in `settings.py` add:
```
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
```
- add the hidden values to the `env.py` file - EMAIL_HOST_PASSWORD can be obtained from [gmail - app passwords](https://myaccount.google.com/apppasswords?pli=1&rapt=AEjHL4MiNMI00Y92NLcRko2H7anRwnL85UsEqLEOAugDkIbMWRZPBCcv6UAcNnLuWInChQvE0FSoYP_xLe_RszCZp4b0NueuVHtLDruGUek8abnMU7YlArw)
- add the same key/value pairs to the `Heroku configvars`
- at the top of `views.py` import:
```
from django.core.mail import send_mail
from django.conf import settings
```
- finally update the `def perform_create` :
```
instance = serializer.save()
subject = f"SHS Contact Form : {instance.subject}"
message = (
    "Senders details\n"
    f"Name: {instance.name}\n"
    f"Email: {instance.email}\n"
    f"Phone: {instance.phone}\n\n"
    f"Subject: {instance.subject}\n"
    f"Message: {instance.message}"
)
from_email = instance.email
to_email = [settings.DEFAULT_FROM_EMAIL]
send_mail(
    subject,
    message,
    from_email,
    to_email,
)
```