from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home_page_views, name='home'),
    path('about/', views.about_page_views, name= 'about'),
    path('author/', views.author_page_views, name= 'author'),
    path('contact/', views.contact_page_views, name= 'contact'),
    path('single_author/', views.single_author_page_views, name= 'single_author'),
]