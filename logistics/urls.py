from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_base, name='select_base'),
    path('<slug:base_name>/home/', views.home, name='home'),
    path('<slug:base_name>/stock/', views.stock, name='stock'),
    path('<slug:base_name>/staff/', views.staff, name='staff'),
    path('<slug:base_name>/distribution/', views.distribution, name='distribution'),
]
