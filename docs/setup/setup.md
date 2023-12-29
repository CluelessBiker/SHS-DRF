### SETUP :
- ```brew install python```
- ```python3.11 --version``` : check version installed
- ```python3.11 -m venv .venv```
- ```.venv/bin/activate```
- access was denied. Ran ```chmod +x .venv/bin/activate``` before running above line again

### resolve issues:
- ```python3.11 -m venv .venv```
- ```source .venv/bin/activate```
- ```. .venv/bin/activate```
### Django :
- ```pip3 install 'django<4'```
- ```django-admin startproject shs_drf .```
- ```pip install django-cloudinary-storage==0.3.0```
- ```python -m pip install Pillow ```
- ```pip3 install djangorestframework```