from django.contrib import admin
from .models import Dessert,DesertCategory

# Register your models here.
admin.site.register(Dessert)
admin.site.register(DesertCategory)