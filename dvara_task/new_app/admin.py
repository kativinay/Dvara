from django.contrib import admin
from .models import *

# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    model = CategoriesModel
    list_display = ('id', 'categories')

class SubCategoriesAdmin(admin.ModelAdmin):
    model = SubCategoriesModel
    list_display = ('id', 'cat_id', 'sub_categories')


admin.site.register(CategoriesModel, CategoriesAdmin)
admin.site.register(SubCategoriesModel, SubCategoriesAdmin)