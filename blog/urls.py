#flake8: NOQA
from django.conf.urls.defaults import *


urlpatterns = patterns('blog.views',
    (ur'^(?P<slug>[\w_]+)/?$', 'post_detail'),
    (ur'^$', 'post_list'),
)
