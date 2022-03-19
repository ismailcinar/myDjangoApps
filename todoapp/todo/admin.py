from django.contrib import admin
from .models import Todo
# Register your models here.
# when we register the models, our models appear the admin panel.
admin.site.register(Todo)