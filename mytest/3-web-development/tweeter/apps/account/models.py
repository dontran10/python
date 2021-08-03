from django.db import models
from django.utils.translation import gettext_lazy as _

# TODO: any DataModel should be placed here
class Post(models.Model):
    content = models.CharField(max_length=256)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this post should be treated as active. '
            'Unselect this instead of deleting posts.'
        ),
    )
