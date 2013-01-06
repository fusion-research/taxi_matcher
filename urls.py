from django.conf.urls.defaults import patterns, include, url
from Site.views import hello,display_meta
from Site.taxi import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^hello/$',hello),
    (r'^taxi/$',views.taxi),
    (r'^search/$', views.search),
    (r'^display/$', display_meta),    
    # Examples:
    # url(r'^$', 'Site.views.home', name='home'),
    # url(r'^Site/', include('Site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
)
