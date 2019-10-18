from django.urls import path, re_path
from django.contrib import admin
from .views import index, library, detail_course
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('biblioteca/', library, name = 'biblioteca'),
    path('biblioteca/<level>/', detail_course, name = 'detalles_curso'),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root':settings.MEDIA_ROOT,
        })
    ]
