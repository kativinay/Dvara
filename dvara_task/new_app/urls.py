from django.urls import path
from new_app.views import CategoriesView, SubCategoriesView

urlpatterns = [
    path('', CategoriesView.as_view(), name='categories_view'),
    path('sub-categories', SubCategoriesView.as_view(), name='sub_categories'),
]