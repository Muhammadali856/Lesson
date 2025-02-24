from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from common.views import home_page_views, about_page_views, author_page_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_views),
    path('about/', about_page_views),
    path('author/', author_page_views),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
