import os
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.views import View
from .models import *
from .forms import SubCategoriesForm

# Create your views here.

class CategoriesView(View):
    """
    GET:    
        GET will return subcategory form in contex to template
        Parameters Required:
            No Parameters Required.

    POST:
        POSt will Insert subcategory form data.
        Parameters Required:
            form fields:
                categories, sub_categories

    Template:
        'new_app/index.html`

    """
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        form = SubCategoriesForm()
        context = {
            'form':form
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        form = SubCategoriesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Form Submitted Successfully.")
            return redirect('/')
        return render(request, self.template_name, {'form': form})

class SubCategoriesView(View):
    """
    GET:
        It wil return subcategory objects.
        parameter Required:
            category
    """

    def get(self, request, *args, **kwargs):
        category = request.GET.get('category')
        if category:
            sub_categories = list(SubCategoriesModel.objects.filter(cat_id=category).values())
        else:
            sub_categories = []
        data = {
            'success':True,
            'sub_categories':sub_categories
        }
        return JsonResponse(data)