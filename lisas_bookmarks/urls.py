from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     #Examples:
     #url(r'^$', 'lisas_bookmarks.views.home', name='home'),
     #url(r'^lisas_bookmarks/', include('lisas_bookmarks.foo.urls')),

     
     #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

     
     #url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls.defaults import*
from project.views import*
urlpatterns=patterns('', (r'^$', main_page),)


