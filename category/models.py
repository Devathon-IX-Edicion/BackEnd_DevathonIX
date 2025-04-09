from django.db import models
from autoslug import AutoSlugField

CATEGORY_CHOICES = (
    ("Common", "Common"),
    ("Rare", "Rare"),
    ("Epic", "Epic"),
    ("Legendary", "Legendary"),
)

class Category(models.Model):   
    name = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name  

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
