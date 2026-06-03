from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.conf.urls.i18n import i18n_patterns
from base.views import change_language
import os

def custom_404(request, exception=None):
    return render(request, '404.html', status=404)

handler404 = custom_404

ADMIN_URL = os.getenv('ADMIN_URL').strip('/')

urlpatterns = [
    path(f'{ADMIN_URL}/', admin.site.urls),
    path('lang/', change_language, name='change_language'),
]

urlpatterns += i18n_patterns(
    path('', include('base.urls')),
    prefix_default_language=False,
)

urlpatterns += [
    re_path(r'^.*$', custom_404),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
