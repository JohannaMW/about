from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from . import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'about.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)