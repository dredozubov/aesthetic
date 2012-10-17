from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    exclude = ('text',)


admin.site.register(Post, PostAdmin)
