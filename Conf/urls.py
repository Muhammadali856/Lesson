from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from test_form.views import test_form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', test_form, name='form'),
    path('', include('common.urls', namespace='pages')),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
