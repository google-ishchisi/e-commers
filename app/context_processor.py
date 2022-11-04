from .models import Category
from store.models import Product
from django.shortcuts import get_object_or_404


def menu_links(request):
    categoriest = Category.objects.all()
    
    return {'categoriest':categoriest}
