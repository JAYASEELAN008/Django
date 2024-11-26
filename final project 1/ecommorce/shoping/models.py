from django.db import models
from django.shortcuts import render



class Category(models.Model):
    name = models.CharField(max_length=255, default=0)


    def __str__(self):
        return self.name

   

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to="products/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    ratings = models.DecimalField(max_digits=2, decimal_places=1, default=0)  # Ratings (e.g., 4.5)
    star_color = models.CharField(max_length=7, default='#FFA500')

    def __str__(self):
        return self.name
    


