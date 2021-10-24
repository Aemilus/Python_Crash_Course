from django.contrib import admin

# Register your models here.

from .models import Plan, Meal

admin.site.register(Plan)
admin.site.register(Meal)
