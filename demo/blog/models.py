from django.db import models
from django.utils.translation import gettext_lazy as _

from django_richtexteditor.fields import RichTextField

class Post(models.Model):

    title = models.CharField(_('title'), max_length=255,
        unique=True,
        help_text=_('The title of the post.')
    )

    # content = models.TextField(_('content'),
        # help_text=_('The content of the post.')
    # )
    # excerpt = models.TextField(_('excerpt'),
        # help_text=_('The excerpt of the post.')
    # )

    content = RichTextField(_('content'),
        help_text=_('The content of the post.')
    )
    excerpt = RichTextField(_('excerpt'),
        help_text=_('The excerpt of the post.')
    )

    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    date_updated = models.DateTimeField(_('date updated'), auto_now=True)

    class Meta:
        verbose_name=_('post')
        verbose_name_plural=_('posts')
        ordering = ('-date_created', 'title',)

    def __str__(self):
        return self.title

