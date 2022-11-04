from django.urls import path
from .views import store, detail

urlpatterns = [
    path('', store, name='store'),
    path('<slug:category_slug>/', store, name='category'),
    path('<slug:category_slug>/<slug:product_slug>/', detail, name='detail'),
]