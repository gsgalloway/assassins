from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'assassins_site.views.home', name='home'),
    # url(r'^assassins_site/', include('assassins_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', RedirectView.as_view(url='http://www.stanford.edu/~gavilan/cgi-bin/assassins')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^assassins/', include('assassins.urls')),
)
