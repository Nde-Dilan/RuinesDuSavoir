from django.contrib import admin

from posts.models import *


# Register your models here.


@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    list_display = ("title",  "published", "created_on", "last_updated")
    list_editable = ("title", "published")
    list_display_links = ("created_on", )


