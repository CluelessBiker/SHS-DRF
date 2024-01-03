### SETUP :

- `brew install python`
- `python3.11 --version` : check version installed
- `python3.11 -m venv .venv`
- `.venv/bin/activate`
- access was denied. Ran `chmod +x .venv/bin/activate` before running above line again

### resolve issues:

- `python3.11 -m venv .venv`
- `source .venv/bin/activate`
- `. .venv/bin/activate`

### Django :

- Start a Django project : `django-admin startproject projectName .`
- Start a Django app : `python3 manage.py startapp AppNameHere`

### PACKAGES :

```
pip3 install 'django<4'
pip install django-cloudinary-storage==0.3.0
python -m pip install Pillow
pip3 install djangorestframework
```

- remember to run `pip3 freeze --local > requirements.txt` at the end of installation

### ENV.PY :

```
import os
os.environ['CLOUDINARY_URL'] = 'cloudinary://yourAPIEnvironmentVariable'
```
