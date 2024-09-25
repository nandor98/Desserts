from django.db import models

# Create your models here.

class DesertCategory(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Dessert(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(DesertCategory,on_delete=models.CASCADE)
    price = models.FloatField()
    image = models.ImageField(upload_to="assets/images/")
    def __str__(self):
        return self.name