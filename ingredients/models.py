from django.db import models
from autoslug import AutoSlugField
from category.models import Category  # asegúrate de importar correctamente

MAGIC_LEVEL_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
)

class Ingredient(models.Model):   
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100, null=False)
    description = models.TextField()
    magic_level = models.CharField(max_length=2, choices=MAGIC_LEVEL_CHOICES)
    image = models.CharField(max_length=100, null=False)
    preparation_time = models.CharField(max_length=100, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name  

    class Meta:
        db_table = 'ingredient'
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'
