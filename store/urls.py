from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('page<int:page_number>/', views.products_by_page, name='CurrentPage'),
    path('search/<str:q>/', views.products_search, name='search_result'),
]