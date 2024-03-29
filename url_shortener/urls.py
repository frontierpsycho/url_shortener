from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'shortener.views.new', name='new'),
    url(r'^url/(?P<id>\d+)$', 'shortener.views.url_detail', name='url_detail'),
    url(r'^(?P<code>\w+)$', 'shortener.views.redirect', name='redirect'),
    # url(r'^url_shortener/', include('url_shortener.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
