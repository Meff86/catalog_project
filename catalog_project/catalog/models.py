from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.name
