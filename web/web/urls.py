from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^add_host/$',  'asset.views.add_host'),
    url(r'^index/$', 'asset.views.index'),
    url(r'^disp_host/(\d+)/$', 'asset.views.disp_host'),
    url(r'^cmd_out/(\d+)/$', 'asset.views.cmd_out'),
)
