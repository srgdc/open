from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'open.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'openapp.views.home', name='home'),
    url(r'^project/(\d+)/$', 'openapp.views.project', name="project"),
)