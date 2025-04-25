from django.db import models

class Effect(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=50)  # tipo de efecto (curación, transformación, etc.)
    rarity = models.CharField(max_length=20)  # común, raro, legendario, etc.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name