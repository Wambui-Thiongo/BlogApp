from django.urls import path
from . import views  # Import views

urlpatterns = [
    path('', views.home, name='home'),  # Add this for the homepage
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('home/', views.home, name='home'),
    path('sidebar/', views.sidebar, name='sidebar'),
]
