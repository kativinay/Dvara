from django.db import models

# Create your models here.

class CategoriesModel(models.Model):
    categories = models.CharField(max_length=30)

    class Meta:
        db_table = 'catogries'
    
    def __str__(self):
        return self.categories

class SubCategoriesModel(models.Model):
    cat_id = models.ForeignKey(CategoriesModel, on_delete=models.CASCADE)
    sub_categories = models.CharField(max_length=30)

    class Meta:
        db_table = 'sub_catogries'
    
    def __str__(self):
        return self.sub_categories


