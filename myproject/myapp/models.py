from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    description = models.TextField(verbose_name='description')
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    description = models.TextField(verbose_name='description')
    def __str__(self):
        return self.name