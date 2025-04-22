from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    magic_level = models.CharField(max_length=2, choices=[
        ("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"),
        ("6", "6"), ("7", "7"), ("8", "8"), ("9", "9"), ("10", "10"),
    ])
    preparation_time = models.PositiveIntegerField()  # Time in minutes
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="ingredients")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name