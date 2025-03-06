from django.urls import path
from .views import blog_list_view, blog_detail_view

app_name = 'blogs'

urlpatterns = [
    path('home', blog_list_view, name='blog-list'),
    path('<int:pk>/', blog_detail_view, name='detail'),
]