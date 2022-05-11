from django.template.context_processors import static
from django.template.defaulttags import url
from django.urls import path, include

from myshop import settings
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('search', views.search, name='search'),
path('filter', views.filter, name='filter'),
]
