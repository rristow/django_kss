from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import django_kss.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_kss_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^styleguide/', include(django_kss.urls)),
)