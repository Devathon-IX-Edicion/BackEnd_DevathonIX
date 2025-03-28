from django.db import models
from autoslug import AutoSlugField

class Category(models.Model):   
    name_category = models.CharField(max_length=100, null=False)
    description   = models.CharField(max_length=100, null=False)
    date_created  = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='name_category')

    def __str__(self):
        return self.name_category  

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
