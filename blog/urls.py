#flake8: NOQA
from django.conf.urls.defaults import *
from blog.feed import LatestEntriesFeed


urlpatterns = patterns('blog.views',
    url(ur'^rss/', LatestEntriesFeed(), name='feed'),
    url(ur'^(?P<slug>[\w_]+)/?$', 'post_detail', name='detail'),
    url(ur'^$', 'post_list', name='list'),
)
