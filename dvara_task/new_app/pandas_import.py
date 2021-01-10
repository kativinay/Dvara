import pandas as pd
import os
import django

# setting up Django script to access model objects without using manage.py shell
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dvara_task.settings')
django.setup()

from new_app.models import CategoriesModel, SubCategoriesModel

def categories(data):
    """
    Insert data into categories table
    """
    if data:
        for i in data:
            category = CategoriesModel(categories=i['categories'])
            category.save()

def subcategories(data):
    """
    Insert data into sub categories table
    """
    if data:
        for i in data:
            cat_obj = CategoriesModel.objects.get(id=i['catid'])
            sub_category = SubCategories(cat_id=cat_obj, sub_categories=i['subcategory'])
            sub_category.save()

def excel_to_json(file_path, sheet=None):
    """
    Return excel data as list of dictionaries by passing file path, sheet name 
    """
    df = pd.read_excel(file_path, sheet_name=sheet)
    columns = [str(k) for k in df.columns]
    data = [dict(zip(columns, row)) for row in df.values]
    return data

