from django.urls import path
from . import views

app_name = 'pages1'

urlpatterns = [
    path('about/', views.about_page_views, name= 'about'),
    path('contact/', views.contact_page_views, name= 'contact'),
    
]