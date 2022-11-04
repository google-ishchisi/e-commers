from django.db import models
from app.models import Category

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField(default=0)

    image = models.ImageField(upload_to='photo/products')
    image2 = models.ImageField(upload_to='photo/products', null=True, blank=True, default=None)
    image3 = models.ImageField(upload_to='photo/products', null=True, blank=True, default=None)
    image4 = models.ImageField(upload_to='photo/products', null=True, blank=True, default=None)
    
    yes_no = models.IntegerField(max_length=100, null=True, blank=True, default=1)

    stock = models.IntegerField(default=0) # Esdan chiqmasin shunga -- (null=True, blank=True) qilish kerak
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        