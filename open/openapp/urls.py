from django.conf.urls import patterns, include, url
from haystack.views import SearchView
from .forms import BasicSearchForm

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'open.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'openapp.views.home', name='home'),
    url(r'^search/', SearchView(form_class=BasicSearchForm), name='haystack_search'),
    url(r'^code/(\d+)/$', 'openapp.views.code', name='code'),
    url(r'^project/(\d+)/$', 'openapp.views.project', name="project"),
    url(r'^submit/$', 'openapp.views.submit', name="submit"),
    url(r'^register/', 'openapp.views.register', name="register"),
    url(r'^logout/', 'openapp.views.logout_view', name="logout"),
)
