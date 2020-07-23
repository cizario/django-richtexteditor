from django.contrib import admin
from django.db import models
from django.utils.translation import gettext, gettext_lazy as _

# from django_richtexteditor.widgets import RichTextarea

from .models import Post


class PostAdmin(admin.ModelAdmin):

    # formfield_overrides = {
        # models.TextField: {'widget': RichTextarea}
    # }
    list_display = ('title',)
    list_per_page = 10
    fields = ('title', 'content', 'excerpt',)


admin.site.register(Post, PostAdmin)
