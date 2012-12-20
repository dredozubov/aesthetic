from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^wanna/write/', include(admin.site.urls)),
    url(r'^posts/', include('blog.urls', namespace='posts')),
    url(ur'^about/$',
        TemplateView.as_view(template_name="about.html"),
        name='about'),
    url(r'^$', 'django.views.generic.simple.redirect_to',
        {'url': '/posts/'},
        name='home'),
)

# media-serving in DEBUG
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
