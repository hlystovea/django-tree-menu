from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.utils.translation import gettext_lazy as _

from core.views import IndexPageView


admin.site.site_title = _('Древовидное меню')
admin.site.site_header = _('Древовидное меню')
admin.site.index_title = _('Администрирование')


urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # noqa (E501)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # noqa (E501)
