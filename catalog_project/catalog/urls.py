from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:brand_id>/<int:category_id>/', views.category_detail, name='category_detail'),
]
