from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Film(models.Model):
    name = models.CharField(max_length=128)
    director = models.CharField(max_length=64)

    tags = TaggableManager()

    def __str__(self):
        return self.name