from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yunwei.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^add_host/$', 'asset.views.add_host'),
    url(r'^index/$', 'asset.views.index'),
    url(r'^disp_host/(\d+)/$','asset.views.disp'),
    url(r'^delete_host/(\d+)/$','asset.views.del_host'),
)
