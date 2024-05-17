from django.db import models


class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    stock = models.IntegerField()
