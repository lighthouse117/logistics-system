from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='logistics/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('select_base/', views.select_base, name='select_base'),
    path('<slug:base_name>/home/', views.home, name='home'),
    path('<slug:base_name>/stock/', views.stock, name='stock'),
    path('<slug:base_name>/stock/input_stock', views.input_stock, name='input_stock'),    
    path('<slug:base_name>/staff/', views.staff, name='staff'),
    path('<slug:base_name>/distribution/', views.distribution, name='distribution'),
    path('<slug:base_name>/distribution/input_distribution', views.input_distribution, name='input_distribution')
]
