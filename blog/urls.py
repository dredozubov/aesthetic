#flake8: NOQA
from django.conf.urls.defaults import *


urlpatterns = patterns('blog.views',
    url(ur'^(?P<slug>[\w_]+)/?$', 'post_detail', name='detail'),
    url(ur'^$', 'post_list', name='list'),
)
