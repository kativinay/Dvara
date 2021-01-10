from django import forms
from .models import CategoriesModel, SubCategoriesModel


class SubCategoriesForm(forms.ModelForm):

    class Meta:
        model = SubCategoriesModel
        fields = "__all__"
        widgets = {
            'cat_id': forms.Select(attrs={'class': 'form-control'}),
            'categories': forms.Select(attrs={'class': 'form-control'}),
        }
       

