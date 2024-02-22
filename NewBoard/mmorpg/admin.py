from django.contrib import admin

from mmorpg.models import Post, Category, Answer

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Answer)