from django.contrib import admin

from .models import Comment, Follow, Group, Post

admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Group)
admin.site.register(Post)
