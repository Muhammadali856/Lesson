from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('', views.home_page_views, name='home'),
    path('author/', views.author_page_views, name= 'author'),
    path('single_author/', views.single_author_page_views, name= 'single_author'),
    path('category/', views.category_page_views, name= 'category'),
    path('blog/', views.blog_page_views, name= 'blog'),
    path('recipe/', views.recipe_page_views, name= 'recipe'),
    path('shop/', views.shop_page_views, name= 'shop'),
]