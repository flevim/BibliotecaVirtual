from django.urls import path, re_path
from django.contrib import admin
from .views import index, library
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('biblioteca/', library),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root':settings.MEDIA_ROOT,
        })
    ]
