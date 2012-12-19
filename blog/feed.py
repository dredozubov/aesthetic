#! -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from blog.models import Post


class LatestEntriesFeed(Feed):
    title = u"Блог Дениса Редозубова"
    link = "/rss/"
    description = u"Обновления блога"

    def items(self):
        return Post.objects.order_by('-created_at')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return ' '.join(item.text.split(u' ')[:20]) + '...'

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('posts:detail', args=[item.slug])
