from django.urls import path
from products.views import *

app_name = 'product'
urlpatterns = [
    path('product/create/', ProductCreateView.as_view()),
    path('all/', ProductListView.as_view()),
    path('product/detail/<int:pk>/', ProductDetailView.as_view())
]